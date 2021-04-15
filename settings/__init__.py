from status import title, splash, select, register, viewcontrols, game, camp
from . import prepare, tools

STATUS_DICT = {
    "SPLASH": splash.Splash(),
    "TITLE": title.Title(),
    "SELECT": select.Select(),
    "REGISTER": register.Register(),
    "CONTROLS": viewcontrols.ViewControls(),
    "GAME": game.Game(),
    "CAMP": camp.Camp()
}


def main():
    """Add states to control here."""
    app = tools.Control(prepare.ORIGINAL_CAPTION)
    app.status_machine.setup_states(STATUS_DICT, "SPLASH")
    app.main()
