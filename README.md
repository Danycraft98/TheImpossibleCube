[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LGPL License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div style="text-align:center">
    <a href="https://github.com/Danycraft98/TheImpossibleCube">
        <img src="static/images/misc/icon.png" alt="Logo">
    </a>
    <h3 style="text-align:center">The Impossible Cube</h3>
    <p style="text-align:center">
        Game Application. The README is still under construction!!
        <br />
        <a href="https://github.com/Danycraft98/TheImpossibleCube/wiki">Explore the docs</a>
        ·
        <a href="https://danycraft98.github.io/TheImpossibleCube/">Read Me Website</a>
        ·
        <a href="https://github.com/Danycraft98/TheImpossibleCube/issues">Report Bug</a>
        ·
        <a href="https://github.com/Danycraft98/TheImpossibleCube/issues">Request Feature</a>
    </p>
</div>

<!-- TABLE OF CONTENTS -->
#### Table of Content
1. [About The Project](#about-the-project)
2. [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact](#contact)
7. [Acknowledgements](#acknowledgements)


<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

The following repository contains all files required to spin up the ECPlaza Tools web-app on Heroku server. As of writing this readme, currently ECPlaza is currently using the web-app. The web-app helps retrieve relevant information for the company to use. The web-app is python-based (python 3.9.1) and uses Django as the main framework. You can view the demo link is available above. Here are the list of applications:


* Spreasheet Comapre Application
* HTML Parser Application
* Traffic Analyzing Application


<!-- GETTING STARTED -->
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [Python 3.9.1](https://python.org/)
* [PyGame (2.0.1)](https://www.pygame.org/)
See the requirements.txt for more PyPi packages you need.
  ```sh
  pip install -r requirements.txt
  ```

### Installation

#### Local Deployment
Make sure you have Python 3.9.1 and mysql installed. 

1. Clone the repo
```sh
$ git clone https://github.com/Danycraft98/TheImpossibleCube.git
$ cd TheImpossibleCube
```
2. Create the virtual environment and install requirements from requirements.txt.
```sh
$ python3 -m venv TheImpossibleCube
$ pip install -r requirements.txt
```
4. Finally, run the application.
```sh
$ python main.py
```

Your app should now be running on [localhost:8000](http://localhost:8000/).


#### Useful Commands
##### Python Commands
???<br/>
`$ python ???`

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://github.com/Danycraft98/TheImpossibleCube/wiki)_



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the LGPL License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Daniel Lee - [@Daniel Lee](https://www.linkedin.com/in/daniel-lee-jhl/) - lee.daniel.jhl@gmail.com

Project Link: [The Impossible Cube](https://github.com/Danycraft98/TheImpossibleCube)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[logo-uri]: static/images/logo.png
[contributors-shield]: https://img.shields.io/github/contributors/Danycraft98/TheImpossibleCube.svg?style=for-the-badge
[contributors-url]: https://github.com/Danycraft98/TheImpossibleCube/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Danycraft98/TheImpossibleCube.svg?style=for-the-badge
[forks-url]: https://github.com/Danycraft98/TheImpossibleCube/network/members
[stars-shield]: https://img.shields.io/github/stars/Danycraft98/TheImpossibleCube.svg?style=for-the-badge
[stars-url]: https://github.com/Danycraft98/TheImpossibleCube/stargazers
[issues-shield]: https://img.shields.io/github/issues/Danycraft98/TheImpossibleCube.svg?style=for-the-badge
[issues-url]: https://github.com/Danycraft98/TheImpossibleCube/issues
[license-shield]: https://img.shields.io/github/license/Danycraft98/TheImpossibleCube.svg?style=for-the-badge
[license-url]: https://github.com/Danycraft98/TheImpossibleCube/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/daniel-lee-jhl/
[product-screenshot]: https://repository-images.githubusercontent.com/337784703/ce9f1180-825e-11eb-8bcc-04a652fb8f1e

Please ignore the notes below this message as it is for my personal safe keeping notes.

### map file color palette
1. home
2. path
3. water color
4. wall (vertical double)
5. wall (horizontal double)
6. wall (horizontal top)
7. wall (vertical left)
8. wall  (vertical right)
9. wall (horizontal bottom)


User [5,5] overworld to edit.map

TODO: add map editor for cutomizable map.