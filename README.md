# Golftionary

Welcome to the ReadMe for the Golftionary. The site is a community driven resource for new and experienced players to learn more about the game of golf. At the moment functionality is basic, with the next goal to add being a coaching section for people to post videos and tips to help people improve.
 
## UX

The deisgn of this website was designed to be relatively simple, so that the users could easily navigate the site and access the information they need.

The defintions page is laid out using mason cards.

## User Stories

### New Visitor

When entering the site the first piece of information that the user comes to is an explanation of what the site does and the information available to them.

Then using the links provided the user can then go onto the list of definitons and find out the infomration they are looking for.

### Registered Visitor

If you are registered to the site you can then login and add/edit the definitions on the site.

## Features

The main two features of the page are the information section and then the map section.

#### Information

The information section of the page is broken into two parts, with two examples of city or beach locations. This section also contains a short description detailing some key points about the destinations.

There is also the current weather for the locations listed here. This weather data is collected using the OpenWeatherMap API and then displayed as a table on the page. This allows the user to make an informed choice about future holidays.

#### Map

The map is there for the users to be able to search any city/location in the world for hotels, restaurants and tourist attractions. The results of this search are then listed in a table to the side, or below on mobile, of the map.

There are then markers on the map, which when clicked give the phone number, Google rating and a link to their website for the result.

#### Future Features

The main feature that would need to be added to this are further pages hosting the companies store front, for the user to spend money with the company.

The other thing to add would be the current time along with the current weather.

## Technologies

* Bootstrap 4 was used to make the structure of the page. This also helps with the responsiveness of the design.
* MongoDB was used to host the database. This was chosen instead of SQL since not all the entries may be complete, so they will have different fields.

## Testing

The login function was tested manually. If you would like to test it wihtout registering please use the Username: NickStevens and the password: test

HTML code was validated using https://validator.w3.org/

CSS code was validated using https://jigsaw.w3.org/css-validator/

## Depoloyment

This site is hosted on GitHub and deployed directly from Heroku. Any commit updates or new releases will be deployed to that master branch. 

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/NickStevens722/Milestone-2 into your terminal. To unlink the site from the GitHub repository, type git remote rm origin into the terminal.

The site is hosted on GitHub and can be run from there or locally by pasting the following link directly into your browser. https://nickstevens722.github.io/Milestone-2/

To view the source code please click on the following GitHub address https://github.com/NickStevens722/Milestone-2

## Credits

Please Note that this site is currently for educational purposes only.