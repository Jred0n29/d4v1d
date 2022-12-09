"""
Module for the use command - used 
to switch between platforms
"""

import platforms
from rich import print
from platforms.platform.cmd import Command, CLISessionState
from platforms.platform import Platform
from types import ModuleType
from typing import *

class Use(Command):
    """
    The use command
    """

    def __init__(self):
        """
        Initializes the use command
        """
        super().__init__('use', aliases=['switch',], description='Switches between platforms')

    def execute(self, args: List[str], state: CLISessionState) -> None:
        """
        Executes the use command

        Args:
            args (List[str]): The arguments
            state (CLISessionState): The session state
        """
        if len(args) == 0:
            if state.platform is not None:
                del state.platform
                state.platform = None
                print(f'[bold grey53][*][/bold grey53] Not using any platform anymore ...')
            return

        platform: str = args.pop(0).lower()
        try:
            p: ModuleType = next(p for n, p in platforms.PLATFORMS.items() if n.lower() == platform)
            if state.platform:
                del state.platform
            state.platform = p.init()
            print(f'[bold grey53][*][/bold grey53] Switched to platform [bold]{platform}[/bold]')
        except StopIteration:
            print(f'[bold red][-][/bold red] Platform [bold]{platform}[/bold] does not exist')