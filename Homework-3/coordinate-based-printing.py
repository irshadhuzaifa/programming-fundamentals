import tcod.console
import tcod.context
import tcod.event
import tcod.tileset


class PlayerState:
    """Example state with a player position."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the player glyph."""
        console.print(self.x, self.y, "@")
        
    def move_up(self, console: tcod.console.Console, dy):
        if self.y - dy >= 0:
            self.y -= dy
    
    def move_down(self, console: tcod.console.Console, dy):
        if self.y + dy < console.height:
            self.y += dy
        
    def move_right(self, console: tcod.console.Console, dx):
        if self.x + dx < console.width:
            self.x += dx
    
    def move_left(self, console: tcod.console.Console, dx):
        if self.x - dx >= 0:
            self.x -= dx

def main():
    tileset = tcod.tileset.load_tilesheet('Alloy_curses_12x12.png', columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437)
    tcod.tileset.procedural_block_elements(tileset=tileset)

    console = tcod.console.Console(80, 50)
    player_state = PlayerState(x=console.width // 2, y=console.height // 2)
    console.print(0, 0, "Hello World!")  # Test text by printing "Hello World" to the console
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:  # Main loop
            console.clear()
            player_state.on_draw(console)
            context.present(console)  # Render the console to the window and show it
            for event in tcod.event.wait():  # Event loop, blocks until pending events exist
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                    
                    if event.sym == tcod.event.KeySym.UP:
                        player_state.move_up(console=console, dy=1)

                    if event.sym == tcod.event.KeySym.DOWN:
                        player_state.move_down(console=console, dy=1)


                    if event.sym == tcod.event.KeySym.LEFT:
                        player_state.move_left(console=console, dx=1)


                    if event.sym == tcod.event.KeySym.RIGHT:
                        player_state.move_right(console=console, dx=1)
    
if __name__ == '__main__':
    main()