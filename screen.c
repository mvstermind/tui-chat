#include <SDL2/SDL.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    // Get the number of displays
    int num_displays = SDL_GetNumVideoDisplays();
    printf("Number of displays: %d\n", num_displays);

    // Iterate through all displays
    for (int i = 0; i < num_displays; i++) {
        SDL_DisplayMode mode;
        
        // Get current display mode of the display
        if (SDL_GetCurrentDisplayMode(i, &mode) != 0) {
            printf("Could not get display mode for display #%d: %s\n", i, SDL_GetError());
            continue;
        }

        printf("Display #%d: %dx%d\n", i, mode.w, mode.h);
    }

    // Quit SDL
    SDL_Quit();
    return 0;
}
