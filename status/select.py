""" Contains classes used for the player selection screen. """
import pygame as pg
import yaml

from settings import prepare, tools, status_machine, menu_functions
from entity import enemy_entity, player
from .constants import *

FONT = pg.font.Font(prepare.FONTS["Fixedsys500c"], 60)  ###
SMALL_FONT = pg.font.Font(prepare.FONTS["Fixedsys500c"], 32)  ###


class Select(status_machine.State):
    """
    This State is updated while our game shows the player select screen.
    This state is made up of four substates to organize updating;
    Options, SelectRegister, Delete, and Confirm.
    """

    def __init__(self):
        status_machine.State.__init__(self)
        self.next = "GAME"
        self.timeout = 15
        self.status_machine = status_machine.StateMachine()

    def startup(self, now, persistant):
        """
        Recreate the substates and substate dict when this state starts up.
        """
        status_machine.State.startup(self, now, persistant)
        state_dict = {"OPTIONS": Options(), "SELECT/REGISTER": SelectRegister(),
                      "DELETE": Delete(), "CONFIRM": Confirm(),
                      "MORE": Options(SECONDARY_OPTIONS), "BACK": Options()}
        self.status_machine.setup_states(state_dict, "OPTIONS")

    def cleanup(self):
        """
        Add variables that should persist to the self.persist dictionary.
        Then reset State.done to False.
        """
        self.done = False
        self.status_machine.done = False
        regi = self.status_machine.state_dict["SELECT/REGISTER"]
        options = self.status_machine.state_dict["OPTIONS"]
        self.persist["save_slot"] = regi.index
        self.persist["player"] = options.players[regi.index]
        return self.persist

    def update(self, keys, now):
        """
        Updates the Cabbages; then the current substate; and finally
        checks to see if the game state or substate needs to change.
        """
        self.status_machine.update(keys, now)
        check_timeout = now - self.start_time > 1000.0 * self.timeout
        if self.status_machine.state_name == "OPTIONS" and check_timeout:
            self.next = "TITLE"
            self.done = True
        elif self.status_machine.done:
            self.next = self.status_machine.state.next
            self.done = True

    def draw(self, surface, interpolate):
        """
        Fill the screen; let the substates handle their own rendering;
        then draw the Cabbages.
        """
        surface.fill(prepare.BACKGROUND_COLOR)
        self.status_machine.state.draw(surface, interpolate)

    def get_event(self, event):
        """
        Get events from Control.
        """
        if event.type == pg.KEYDOWN:
            self.start_time = pg.time.get_ticks()
        self.status_machine.get_event(event)


class SelectState(menu_functions.BasicMenu):
    """Base class for all Select state substates."""

    def __init__(self, option_length):
        menu_functions.BasicMenu.__init__(self, option_length)
        self.rendered = {}

    def draw_player(self, surface, player_sprite, index, redraw=False):
        """
        Draw the player in slot index.  Setting the redraw flag allows for
        the player to be animated.
        """
        if player_sprite != "EMPTY":
            if player_sprite.image and not player_sprite.redraw:
                player_sprite.redraw = redraw
            player_sprite.direction = "front"
            player_sprite.adjust_frames(pg.time.get_ticks())
            expand = pg.transform.scale(player_sprite.image, (100, 100))
            player_sprite.direction = player_sprite.start_direction  ###
            player_sprite.redraw = redraw  ###
            position = (PLAYER_START[0], PLAYER_START[1] + SLOT_SPACER * index)
            surface.blit(expand, position)
            self.draw_player_stats(surface, player_sprite, index)

    def draw_player_stats(self, surface, player_sprite, index):
        """Draw the player's key items and stats to their character slot."""
        items = prepare.GFX["misc"]["sidebargfx"].subsurface(20, 160, 80, 100)
        icons = prepare.GFX["misc"]["icons"]
        surface.blit(items, (ITEM_IMAGES[0], ITEM_IMAGES[1] + index * SLOT_SPACER))
        for i, stat in enumerate(["money", "keys"]):
            num = player_sprite.inventory[stat]
            pos_y = ITEM_START[1] + index * SLOT_SPACER + i * ITEM_SPACER
            rend_it = (SMALL_FONT, str(num), pg.Color("white"), self.rendered)
            surface.blit(tools.get_rendered(*rend_it), (ITEM_START[0], pos_y))
        speed = "{:.1f}".format(player_sprite.speed * 2)
        pos = STAT_START[0], STAT_START[1] + SLOT_SPACER * index
        surface.blit(icons, pos, (0, 0, 34, 34))
        rend_it = (SMALL_FONT, speed, pg.Color("white"), self.rendered)
        rendered = tools.get_rendered(*rend_it)
        surface.blit(rendered, (pos[0] + STAT_TEXT_SPACE, pos[1]))


class Options(SelectState):
    """
    Essentially the main menu state of the whole game.
    """

    def __init__(self, options=OPTIONS):
        SelectState.__init__(self, 3)
        self.players = self.load_players()
        self.names = self.make_player_names()
        self.opt_const = options
        self.options = self.make_options(FONT, options, OPT_Y, OPT_SPACER)
        self.image = pg.Surface(prepare.SCREEN_SIZE).convert()
        self.image.set_colorkey(prepare.COLOR_KEY)
        self.image.fill(prepare.COLOR_KEY)

    def startup(self, now, persistant):
        """Reload all players and rerender their names on startup."""
        status_machine.State.startup(self, now, persistant)
        self.image.fill(prepare.COLOR_KEY)
        self.players = self.load_players()
        self.names = self.make_player_names()

    def load_players(self):
        """
        Load player settings.  If no settings is find create three empty slots.
        """
        players = ["EMPTY", "EMPTY", "EMPTY"]
        try:
            with open(prepare.SAVE_PATH) as my_file:
                data = yaml.load(my_file)
            for i, play_data in enumerate(data):
                if play_data != "EMPTY":
                    players[i] = player.Player(play_data)
        except IOError:
            pass
        return players

    def make_player_names(self):
        """
        Return a list of (name,rect) tuples for each player in self.players.
        """
        names = []
        for i, player in enumerate(self.players):
            try:
                message = FONT.render(player.name, 0, pg.Color("white"))
            except AttributeError:
                message = FONT.render(player, 0, pg.Color("white"))
                args = FONT, player, pg.Color("white"), (0, 0)
            pos = NAME_START[0], NAME_START[1] + SLOT_SPACER * i
            rect = message.get_rect(topleft=pos)
            names.append((message, rect))
        return names

    def cleanup(self):
        """
        Add variables that should persist to the self.persist dictionary.
        Then reset State.done to False.
        """
        self.done = False
        self.persist["options_bg"] = self.image
        self.persist["players"] = self.players
        return self.persist

    def pressed_enter(self):
        """Enter next substate or view the controls screen on enter."""
        self.next = self.opt_const[self.index]
        if self.next == "DELETE":
            if not all(player == "EMPTY" for player in self.players):
                self.done = True
        elif self.next in ["CONTROLS", "EXIT"]:
            self.quit = True
        else:
            self.done = True

    def draw(self, surface, interpolate):
        """
        Blit the base image and options to a seperate surface for later use.
        Then blit that surface and the players to the screen.
        """
        self.image.blit(prepare.GFX["misc"]["charcreate"], MAIN_TOP_LEFT)
        for name_info in self.names:
            self.image.blit(*name_info)
        for i, val in enumerate(self.opt_const):
            which = "selected" if i == self.index else "unselected"
            msg, rect = self.options[which][i]
            self.image.blit(msg, rect)
        surface.blit(self.image, (0, 0))
        for i, player_sprite in enumerate(self.players):
            self.draw_player(surface, player_sprite, i)


class CharHighlighter(SelectState):
    """
    Both substates SelectRegister and Delete inherit from this class.
    Contains the logic for drawing the player selection highlight cursor.
    """

    def __init__(self):
        SelectState.__init__(self, 3)
        self.highlight_rect = pg.Rect(129, 83, 942, 124)

    def draw(self, surface, interpolate):
        """
        Draw the highlight first; then the base screen image; finally draw
        the players, animating the currently selected player.
        """
        highlight = self.highlight_rect.move(0, SLOT_SPACER * self.index)
        surface.fill(HIGHLIGHT_COLOR, highlight)
        surface.blit(self.persist["options_bg"], (0, 0))
        for i, player_sprite in enumerate(self.persist["players"]):
            redraw = i == self.index
            self.draw_player(surface, player_sprite, i, redraw)

    def pressed_exit(self):
        """Return to options menu."""
        self.done = True
        self.next = "OPTIONS"


class SelectRegister(CharHighlighter):
    """State for selecting (or creating a new) character."""

    def __init__(self):
        CharHighlighter.__init__(self)

    def pressed_enter(self):
        """
        If a already created player is selected, enter game with that player;
        Else enter the "register a new player" state.
        """
        if self.persist["players"][self.index] != "EMPTY":
            self.quit = True
            self.next = "GAME"
        else:
            self.quit = True
            self.next = "REGISTER"


class Delete(CharHighlighter):
    """
    Substate updates when the Delete option is selected from the option menu.
    """

    def __init__(self):
        CharHighlighter.__init__(self)

    def pressed_enter(self):
        """
        If there is a player at the selected index, enter confirm substate.
        """
        if self.persist["players"][self.index] != "EMPTY":
            self.done = True
            self.next = "CONFIRM"

    def cleanup(self):
        """
        Add the index of the potentially deleted player to the persist dict
        so that we can access it as needed from the Confirm substate.
        """
        self.done = False
        self.persist["del_index"] = self.index
        return self.persist


class Confirm(SelectState):
    """
    Select substate that updates when the user is asked to confirm the
    deletion of a character.
    """

    def __init__(self):
        self.box_image = prepare.GFX["misc"]["delete"]
        centerx = prepare.SCREEN_RECT.centerx
        top = MAIN_TOP_LEFT[1] + 130
        self.rect = self.box_image.get_rect(centerx=centerx, top=top)
        SelectState.__init__(self, 2)
        self.options = self.make_options(SMALL_FONT, ["Confirm", "Cancel"], self.rect.y + 130, 35)
        self.player = None

    def startup(self, now, persistant):
        """
        Make options default to Cancel to be polite.
        Set the currently selected player's hit_state so they damage strobe.
        """
        status_machine.State.startup(self, now, persistant)
        del_index = self.persist["del_index"]
        self.player = self.persist["players"][del_index]
        self.player.hit_state = True
        self.index = 1

    def draw(self, surface, interpolate):
        """
        Draw the background, players, delete window and options.
        """
        surface.blit(self.persist["options_bg"], (0, 0))
        for i, player_sprite in enumerate(self.persist["players"]):
            redraw = i == self.persist["del_index"]
            self.draw_player(surface, player_sprite, i, redraw)
        surface.blit(self.box_image, self.rect)
        for i in (0, 1):
            which = "selected" if i == self.index else "unselected"
            msg, rect = self.options[which][i]
            surface.blit(msg, rect)

    def save_change(self):
        """
        Overwrite the save settings of the player with
        the string EMPTY.
        """
        with open(prepare.SAVE_PATH) as my_file:
            data = yaml.load(my_file)
        del_index = self.persist["del_index"]
        data[del_index] = "EMPTY"
        with open(prepare.SAVE_PATH, 'w') as my_file:
            yaml.dump(data, my_file)

    def pressed_enter(self):
        """
        Return to menu on 'Cancel'; set player to 'dead' on 'Confirm'.
        """
        if not self.index:
            self.player.action_state = "dead"
        else:
            self.pressed_exit()

    def update(self, keys, now):
        """
        If a player deletion has been confirmed and death animation completed,
        return to menu.
        """
        if self.player.death_anim.done:
            self.save_change()
            self.pressed_exit()

    def get_event(self, event):
        """Don't process events if a player deletion has been confirmed."""
        if self.player.action_state != "dead":
            SelectState.get_event(self, event)

    def pressed_exit(self):
        """Return to options menu."""
        self.done = True
        self.next = "OPTIONS"
