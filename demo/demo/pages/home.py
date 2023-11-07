"""The home page of the app."""
import reflex as rx

from ..styles import *


def home_page() -> rx.Component:
    """The UI for the home page.

    Returns:
        rx.Component: The UI for the home page.
    """
    return rx.box(
        rx.vstack(
             rx.heading(
                "Welcome! 👋",
                font_size="2.5em",
            ),
             rx.image(
                src="/reflex_landing.png",
                width="100%",
            ),
            rx.text(
                "Reflex is an open-source app framework that allows you to build web apps in pure python.",
            ),
            rx.text(
                "Select a demo from the sidebar to see some examples of what Reflex can do!"
            ),
            rx.heading(
                "Things to check out:",
                font_size="2em",
            ),
            rx.unordered_list(
                rx.list_item(
                    "Take a look at ",
                    rx.link(
                        "reflex.dev",
                        href="https://reflex.dev",
                        color="rgb(107,99,246)",
                    ),
                ),
                rx.list_item(
                    "Check out our ",
                    rx.link(
                        "docs",
                        href="https://reflex.dev/docs/getting-started/introduction/",
                        color="rgb(107,99,246)",
                    ),
                ),
                rx.list_item(
                    "Ask a question in our ",
                    rx.link(
                        "community",
                        href="https://discord.gg/T5WSbC2YtQ",
                        color="rgb(107,99,246)",
                    ),
                ),
                padding_left="1.5rem",
            ),
            style=template_content_style,
        ),
        style=template_page_style,
    )
