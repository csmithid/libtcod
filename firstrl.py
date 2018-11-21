import tcod
from input_handlers import handle_keys

def main():
    screen_width = 36
    screen_height = 36

    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

    tcod.console_set_custom_font('terminal8x8_gs_ro.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_ASCII_INROW)
    root = tcod.console_init_root(screen_width,screen_height,'roguelike', False)

    con = tcod.console_new(screen_width, screen_height)

    key = tcod.Key()
    mouse = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)
        tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_blit(con, 0, 0, screen_width, screen_height, root, 0, 0)
        tcod.console_flush()
        tcod.console_clear(con)

        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx,dy = move
            player_x += dx
            player_y += dy

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
if __name__ == '__main__':
    main()
