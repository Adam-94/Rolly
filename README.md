[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Adam-94/Devstats/blob/master/LICENSE)
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/adam-94/Rolly">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Rolly</h3>

  <p align="center">
    Rolly is a simple Dungeons & Dragons Dice roller with an additional ability to look up items, races, spells and so on. 
    <br />
    <a href="https://discord.com/api/oauth2/authorize?client_id=706590530418638911&permissions=0&scope=bot">Add Rolly to your server</a>
    ·
    <a href="https://github.com/adam-94/Rolly/issues">Report Bug</a>
    ·
    <a href="https://github.com/adam-94/Rolly/issues">Request Feature</a>
  </p>
</p>

## Table of Contents

* [About the Project](#about-the-project)
  * [Commands](#commands)
  * [Built With](#built-with)
* [Contributing](#contributing)
* [License](#license)

<!-- ABOUT THE PROJECT -->
## About The Project
![roll command](images/roll.gif)  ![find command](images/find.gif)

As stated above, Rolly is a Dungeons & Dragons dice roller made as a introduction into how Discord bots are created. Due to the COVID-19 pandemic, playing with friends in person became no longer possible. This seemed like a fitting creation to make for online play during those times.

## Commands

Rolly isn't a bot with an excess amount of features, so the commands are easy to memorise and learn. 
It does the main basic things you'll need to get going in a Dungeons & Dragons game. 

##### Roll Command

With the roll command, we can do straight, advantage/disadvantage and modifier rolls.

1. Straight roll 
```sh
    -roll 1d20
```
2. Advantage/Disadvantage roll 
```sh
    -roll 2d20
```
3. Modifier roll
```sh
    -roll 1d20+5
```

##### Find Command

The find command is a nifty quick way of getting information on items, races, spells and so on. This works by searching an online compendium with the query and returning an image file.

1. Basic find
```sh
    -find potion_of_healing
```

### Built With
* [Python](https://www.python.org/)
* [discord.py](https://discordpy.readthedocs.io/en/latest/)
* [Selenium](https://www.selenium.dev/documentation/en/)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [dnd5tools](http://radai.github.io/dnd5tools/)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/adam-94/Rolly.svg?style=flat-square
[forks-url]: https://github.com/adam-94/Rolly/network/members
[stars-shield]: https://img.shields.io/github/stars/adam-94/Rolly.svg?style=flat-square
[stars-url]: https://github.com/adam-94/Rolly/stargazers
[issues-shield]: https://img.shields.io/github/issues/adam-94/Rolly.svg?style=flat-square
[issues-url]: https://github.com/adam-94/Rolly/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/adam-hughes-a2a1a115a
[product-screenshot]: images/screenshot.png