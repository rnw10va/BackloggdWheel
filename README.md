# Media Selection Wheel

Progress on hold temporarily due to life obligations and determining if I should make changes to how I created the GUI.


Summary
This wheel will take a Backloggd or IMDB link, place all the media on the page into a wheel, and then randomly select one of the values via spinning it.


Setup
Coming soon...


Detailed Explanation
The goal of this project was to be able to take a page or list from a website with media listed on it, such as IMDB for movies/tv and Backloggd for video games, then place all the media from that page into a wheel and allow the user to spin it to make a random determination as to what to watch or play.

I finished the project in terms of basic functionality. The code can take items listed from an IMDB or Backloggd web page and place it into a wheel. The wheel can be spun and will land on one of the choices. The spinning speed starts fast, slows down, and then eventually stops. The code can use any number of items in the wheel, so the amount of media on the webpage will work no matter how many items there are.


Technical Summary
I used Python 3.12.4 with PyQT6 for the GUI and the requests library to obtain the web page. The main reason I used Python originally for web scraping, and then I stuck to it so that (hopefully) it would be extremely easy for someone to run the code, even with no programming knowledge. Visual Studio Code and Python 3.12.4 can both both be obtained from the Microsoft Store, which helps with the simplicity in my opinion. I used a Model-View-Controller design pattern primarily because it was what I already knew how to use.


Future Goals (In No Order)
 - Make the wheel less choppy while spinning on less powerful hardware.
 - Zoom into the wheel if there are too many options (~35+) so that the user can see the text properly for each choice as the GUI becomes extremely crowded.
 - Adjust font size and positioning better based on how many slices the wheel has. The text can look a little out of place sometimes (slightly too far left or right for example).
 - Make the wheel look better if there are 6 or fewer items in it. I had to create the pizza slice myself as the library I used didn’t have one, and the trigonometry equation I created doesn’t look perfectly round with that few slices.
 - Add more website functionality, such as Rotten Tomatoes or Metacritic.
