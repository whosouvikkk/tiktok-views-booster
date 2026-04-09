import requests
import validators
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

console = Console()

WEBHOOK_URL = "https://discord.com/api/webhooks/1468202264849285276/8ArPVQreUK9YjVFweq3sdr4mccLPMsfyrtImmNKC7EGXf32XP4RL9e99RVeqP-JzgQnc"
DISCORD_INVITE = "https://discord.gg/eG3KwUXcmB"


def show_header():
    console.clear()
    header_text = """
[bold cyan]
     ██╗███████╗███████╗████████╗     ████████╗ ██████╗  ██████╗ ██╗     
     ██║██╔════╝██╔════╝╚══██╔══╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
     ██║█████╗  █████╗     ██║           ██║   ██║   ██║██║   ██║██║     
██   ██║██╔══╝  ██╔══╝     ██║           ██║   ██║   ██║██║   ██║██║     
╚█████╔╝███████╗███████╗   ██║           ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚════╝ ╚══════╝╚══════╝   ╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
[/bold cyan]
"""
    console.print(Align.center(header_text))
    console.print(Align.center("[yellow]📦 Simple Python CLI Tool | Demo / Educational Use Only[/yellow]\n"))


def show_menu():
    menu = Panel(
        "[bold white]1.[/bold white] Tiktok Views Service\n[bold white]2.[/bold white] Exit",
        title="[bold cyan]MAIN MENU[/bold cyan]",
        border_style="cyan",
        box=box.DOUBLE
    )
    console.print(menu)



def get_valid_username():
    while True:
        username = Prompt.ask("[cyan]Enter Username[/cyan]").strip()
        if username:
            return username
        console.print("[red]Username cannot be empty![/red]")


def get_valid_link():
    while True:
        link = Prompt.ask("[cyan]Enter Video Link[/cyan]").strip()
        if validators.url(link):
            return link
        console.print("[red]Invalid URL! Enter a valid link.[/red]")


def get_valid_amount():
    while True:
        amount = Prompt.ask("[cyan]Enter Amount [/cyan]").strip()
        
        if not amount.isdigit():
            console.print("[red]Amount must be numeric![/red]")
            continue
        
        amount = int(amount)

        if 100 <= amount <= 5000:
            return amount
        
        console.print("[red]Amount must be between 100 and 5000![/red]")



def send_to_webhook(username, link, amount):
    payload = {
        "content": f"New Order 🚀\n\nUsername: {username}\nLink: {link}\nAmount: {amount}"
    }

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[cyan]Sending order...[/cyan]"),
            transient=True
        ) as progress:
            progress.add_task("send", total=None)
            response = requests.post(WEBHOOK_URL, json=payload)

        if response.status_code == 204:
            return True
        else:
            console.print(f"[red]Webhook failed! Status: {response.status_code}[/red]")
            return False

    except Exception as e:
        console.print(f"[red]Error sending webhook: {e}[/red]")
        return False


def tvs_flow():
    console.print("\n[bold green]🚀 Tiktok Views Service Selected[/bold green]\n")

    username = get_valid_username()
    link = get_valid_link()
    amount = get_valid_amount()

    success = send_to_webhook(username, link, amount)

    if success:
        console.print("\n[bold green]✅ Your one-time trial credit has been used. The order will be delivered within 12 hours. For additional views, purchase a key from the Discord server below. Further orders without a key will not be processed.[/bold green]")
        console.print(f"[bold cyan]👉 Join: {DISCORD_INVITE}[/bold cyan]\n")
    else:
        console.print("[red]❌ Failed to process request.[/red]")


def main():
    while True:
        show_header()
        show_menu()

        choice = Prompt.ask("\n[cyan]Select Option[/cyan]")

        if choice == "1":
            tvs_flow()
            Prompt.ask("\n[grey]Press Enter to continue[/grey]")
        elif choice == "2":
            console.print("[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[red]Invalid choice![/red]")


if __name__ == "__main__":
    main()