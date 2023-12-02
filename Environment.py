import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 10
CELL_SIZE = 50  # Adjusted size for 8x8 grid within a 16x16 screen
SCREEN_SIZE = (800, 800)  # Added space for scores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.score = 0
        self.image = pygame.image.load(image_path)
        self.initial_x = x  # Store the initial x position
        self.initial_y = y  # Store the initial y position

    def reset(self):
        # Reset the player's state to the initial position and score
        self.x = self.initial_x
        self.y = self.initial_y
        self.score = 0

    def move(self, dx, dy):
        new_x = (self.x + dx) % GRID_SIZE
        new_y = (self.y + dy) % GRID_SIZE

        # Check if the new position is within the boundaries
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            self.x = new_x
            self.y = new_y
        else:
            # Handle the case when the new position is outside the boundaries
            pass

    def dash(self, other_player):
        self.score += 1
        other_player.score -= 0.5

# Initialize players
player1 = Player(0, 0, "player1.jpg")
player2 = Player(0, GRID_SIZE - 1, "player2.jpg")
player3 = Player(GRID_SIZE - 1, 0, "player3.jpg")
player4 = Player(GRID_SIZE - 1, GRID_SIZE - 1, "player4.jpg")

players = [player1, player2, player3, player4]

# Initialize Pygame screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Player Dash Game")

# Load car images
car_images = [
    pygame.image.load("player1.jpg"),
    pygame.image.load("player2.jpg"),
    pygame.image.load("player3.jpg"),
    pygame.image.load("player4.jpg"),
]

# Game loop
start_time = time.time()
game_duration = 40  # seconds
while time.time() - start_time < game_duration:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movements
    for player in players:
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        player.move(dx, dy)

        # Check if players dash each other
        for other_player in players:
            if player != other_player and player.x == other_player.x and player.y == other_player.y:
                player.dash(other_player)
                print(f"Player {players.index(player) + 1} dashed Player {players.index(other_player) + 1}")

    # Draw the grid and players
    screen.fill(WHITE)
    
    # Draw the scores above the grid
    font = pygame.font.Font(None, 20)
    for i, player in enumerate(players):
        score_text = font.render(f"Player {i + 1} Score: {player.score}", True, RED)
        screen.blit(score_text, (10 + i * 200, 550))

    # Draw the time remaining on the right side
    remaining_time = max(0, game_duration - (time.time() - start_time))
    time_text = font.render(f"Time: {int(remaining_time)} seconds", True, RED)
    screen.blit(time_text, (SCREEN_SIZE[0] - time_text.get_width() - 10, 10))

    # Draw the grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, (200, 200, 200), (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Draw the car images
    for i, player in enumerate(players):
        car_image = pygame.transform.scale(car_images[i], (CELL_SIZE, CELL_SIZE))
        screen.blit(car_image, (player.x * CELL_SIZE, player.y * CELL_SIZE))

    pygame.display.flip()
    pygame.time.delay(500)  # Delay to slow down the game for visualization purposes
    
# Find the winner
winner = max(players, key=lambda player: player.score)

# Display the winners and their scores for 2 seconds
screen.fill(WHITE)
if winners:
    if len(winners) == 1:
        winner_text = font.render(f"Winner: Player {players.index(winners[0]) + 1} - Score: {winners[0].score}", True, RED)
        screen.blit(winner_text, (SCREEN_SIZE[0] // 2 - winner_text.get_width() // 2, SCREEN_SIZE[1] // 2 - winner_text.get_height() // 2))
    else:
        winners_text = font.render("Winners:", True, RED)
        screen.blit(winners_text, (SCREEN_SIZE[0] // 2 - winners_text.get_width() // 2, SCREEN_SIZE[1] // 2 - winners_text.get_height() // 2))

        y_offset = SCREEN_SIZE[1] // 2
        for winner in winners:
            winner_text = font.render(f"Player {players.index(winner) + 1} - Score: {winner.score}", True, RED)
            screen.blit(winner_text, (SCREEN_SIZE[0] // 2 - winner_text.get_width() // 2, y_offset))
            y_offset += winner_text.get_height()

pygame.quit()
sys.exit()