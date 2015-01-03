Academicons
===========
Academicons is an icon font for academics. It aims to supplement other packages (such as Font Awesome) with icons for websites such as Google Scholar, ResearchGate, and Mendeley.

##License
- The Academicons font is licensed under the SIL OFL 1.1:
  - http://scripts.sil.org/OFL
- Academicons CSS, LESS, and SASS files are licensed under the MIT License:
  - http://opensource.org/licenses/mit-license.html
- The Academicons documentation is licensed under the CC BY 3.0 License:
  - http://creativecommons.org/licenses/by/3.0/

##Author
- GitHub: https://github.com/dtnedry

##Icons
`google-scholar`
`google-scholar-square`
`researchgate`
`researchgate-square`
`mendeley`
`mendeley-square`
`orcid`
`orcid-square`
`impactstory`
`impactstory-square`
`academia`
`academia-square`
`zotero`
`zotero-square`
`figshare`
`figshare-square`

##How to use

###Alongside Font Awesome
Academicons was built as a supplement to Font Awesome, which means that the two fonts share the same metrics. To use alongside an existing Font Awesome installation, place the `fonts` folder and the `academicons.css` stylesheet in the same directory on your server and link to the stylesheet using:

    <link rel="stylesheet" href="/path/to/folder/academicons.css" />

Make sure that this link appears before the link for the Font Awesome CSS, or else it will interfere with the `fa-` classes. Call the icons in the same way as you would using Font Awesome, but replacing `fa` with `ai`:

    <i class="ai ai-google-scholar-square fa-3x"></i>

All of the Font Awesome styling classes (such as `fa-3x`, `fa-spin`, etc.) can be used with Academicons.

###With IcoMoon
The SVG font (`fonts/academicons.svg`) can be readily imported into the IcoMoon App (https://icomoon.io/app/), allowing you to merge only the icons that you want into your icon set.
