using System;

namespace ConsoleGame
{
    class Game : SuperGame
    {

        public new static void UpdatePosition(string key, out int xChange, out int yChange)
        {
            yChange = 0;
            xChange = 0;
            switch (key)
            {
                case ("DownArrow"):
                    yChange += 1;
                    xChange = 0;
                    break;
                case ("RightArrow"):
                    xChange += 1;
                    yChange = 0;
                    break;
                case ("LeftArrow"):
                    xChange -= 1;
                    yChange = 0;
                    break;
                case ("UpArrow"):
                    yChange -= 1;
                    xChange = 0;
                    break;
                default:
                    yChange = 0;
                    xChange = 0;
                    break;
            }
        }

        public new static char UpdateCursor(string key)
        {
            switch (key)
            {
                case ("DownArrow"):
                    return 'v';
                    break;
                case ("RightArrow"):
                    return '>';
                    break;
                case ("LeftArrow"):
                    return '<';
                    break;
                case ("UpArrow"):
                    return '^';
                    break;
                default:
                    return 'ö';
                    break;
            }
        }

        public new static int KeepInBounds(int current, int max)
        {
            if (current < 0)
            {
                return max -1;
            }

            if (current >= max)
            {
                return 0;
            }

            return current;
        }

        public new static bool DidScore(int playerX, int playerY, int fruitX, int fruitY)
        {
            if (playerX == fruitX && playerY == fruitY)
            {
                return true;
            }
            return false;
        }
    }
}