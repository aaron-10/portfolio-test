import os

def generate_html(title, year):
    # Create the HTML content with variables
    html_content = f"""
    <!DOCTYPE HTML>
    <!--
    	Verti by HTML5 UP
    	html5up.net | @ajlkn
    	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
    -->
    <html>

    <head>
        <title>{title} {year}</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="assets/css/main.css" />
    </head>

    <body class="is-preload homepage">
        <div id="page-wrapper">

            <!-- Main -->
            <div id="main-wrapper">

                <button class="small" onclick="history.back()">
                    &#8592; Back
                </button>

                <div class="container">
                    <div id="content">
                        <!-- Content -->
                        <div class="row gtr-200">
                            <div class="col-8 col-12-medium off-1 ">
                                <article>
                                    <h2>{title}<span class="yearspan">{year}</span></h2>
                                </article>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Main -->
            <div id="features-wrapper">
                <div class="container">
                    <div class="row gtr-200">
                        <div class="col-10 col-12-medium off-1">
                            <div id="content">
                                <!-- Content -->
                                <article>
                                    <img src="images/jib2.jpg" class="image right" width="40%">
                                    <h3>Overview</h3>
                                </article>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Scripts -->
            <script src="assets/js/jquery.min.js"></script>
            <script src="assets/js/jquery.dropotron.min.js"></script>
            <script src="assets/js/browser.min.js"></script>
            <script src="assets/js/breakpoints.min.js"></script>
            <script src="assets/js/util.js"></script>
            <script src="assets/js/main.js"></script>

        </div>
    </body>

    </html>
    """

    # Generate filename based on title
    sanitized_title = title.replace(" ", "-").lower()
    filename = f"p-{sanitized_title}.html"

    # Write the HTML content to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f"File '{filename}' generated successfully.")

# Variables to change
h2_content = "Solar Boat Twente visuals"
year = "2024"

# Generate the HTML file
generate_html(h2_content, year)
