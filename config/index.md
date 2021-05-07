---
layout: home
---

<div class="container">
  <div class="row">
<% @glyphs.each do |name, value|
  unless name.end_with? "-square"
%>
    <div class="col-2 center ai-case">
      <i class="ai ai-<%= name %> ai-4x"></i>
      <%= name %>
    </div>
<% end
end%>
  </div>
</div>

# What is Academicons?

Academicons is a specialist icon font for academics. It contains icons for websites and organisations related to academia that are often missing from mainstream font packages. It can be used by itself, but its primary purpose is to be used as a supplementary package alongside a larger icon set.

**All product names, logos, and brandsare are the property of their respective owners. Use of these names, logos, and brands does not imply endorsement.**

# How do I use it?

## Alongside Font Awesome

Academicons was originally built as a supplement to [Font Awesome 5](https://github.com/FortAwesome/Font-Awesome), so the two fonts intentionally share the same metrics. You can [style](/academicons/usage) the icons using Font Awesome CSS controls.

There are two ways to install Academicons on your site. The most reliable way is to place the `fonts` and `css` folders on your server and link to the `academicons.css` stylesheet by adding the following to the page header:

{% highlight html %}

<link rel="stylesheet" href="/path/to/folder/css/academicons.min.css"/>

{% endhighlight %}

Alternatively, use the jsdelivr CDN to call the most recent version of Academicons from the content distribution network.

Load Academicons v1 (latest release in the 1.x.x range; recommended):

{% highlight html %}

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">

{% endhighlight %}

Or get the latest version (not recommended) using:

{% highlight html %}

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons/css/academicons.min.css">

{% endhighlight %}

Call the icons in the same way as you would using Font Awesome, but replacing `fa` with `ai`. For example:

{% highlight html %}

<i class="ai ai-google-scholar-square ai-3x"></i>

{% endhighlight %}

**Note:** Each icon also has an associated `-square` icon to enable better integration with the square Font Awesome icons.

## With font building apps

The `academicons.svg` font file can be readily imported into most font building apps, allowing you to merge only the icons that you want into your personalised icon set.

## Desktop publishing

The font files can be installed locally on your system, allowing access to the icons through most publishing software. You can also access the full set of icons in LaTeX using the [Academicons package](http://www.ctan.org/pkg/academicons).

# Requesting new icons

New icons can be requested by creating an issue [here](https://github.com/jpswalsh/academicons/issues). Before submitting a request, please check that the following conditions are satisfied:

  * The organisation in question is already using a logo/icon of appropriate dimensions (roughly 1 × 1). If that doesn't exist, then there's really not much that can be done, and the request will have to be ignored until such time that a logo/icon can be provided.

  * An icon of appropriate resolution can be provided or linked to. Ideally, the provided file will be a vector file (*e.g.* SVG, EPS, AI) or a PDF with the vector file embedded. These files are all very easy to work with, and result in the most faithful reproductions of the icon. Altenatively, high resolution raster images (*e.g.* JPEG, PNG, GIF) can work, but only if the resolution is high enough that the underlying shapes can be reproduced. Icons made from raster images take much longer to prepare, and require hand drawing each component and figuring out the exact typeface used for any letters. This process can be rather tedious, and I will only do this if there is significant demand for the icon. Favicon files can be useful in conjunction with larger logos that have non-ideal aspect ratios—where they can indicate which part of the logo to strip down to—but they are pretty much useless by themselves. The only time I have made an icon from a favicon was for arXiv, and that was only because: (i) It was heavily requested, and (ii) I was able to get feedback on the new icon from Paul Ginsparg, who made the original icon. You can still submit the request, but it will likely be ignored until someone else comes along and provides the file we need.

  * The icon can be reduced to monochrome. This is one of the basic requirements of a versatile icon, but it is often overlooked when icons are made by people who are not professional designers. Academia is full of unprofessional designers, and it is sometimes the case that a logo relies entirely on the use of different colours. In certain cases we can be creative (see the dblp logo), but more often than not it will be impossible to create a monochrome version of the icon. Again, feel free to make the request, but it will probably be ignored if an alternate logo cannot be found.

# License

- The Academicons font is licensed under the SIL OFL 1.1:
  - [http://scripts.sil.org/OFL](http://scripts.sil.org/OFL)
- Academicons CSS, LESS, and SASS files are licensed under the MIT License:
  - [http://opensource.org/licenses/mit-license.html](http://opensource.org/licenses/mit-license.html)
- The Academicons documentation is licensed under the CC BY 3.0 License:
  - [http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/)

# Author

- GitHub: [https://github.com/jpswalsh](https://github.com/jpswalsh)
- Web: [http://jpswalsh.com](http://jpswalsh.com)
