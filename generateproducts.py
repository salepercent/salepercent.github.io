import csv
import os
import re

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the CSV directory as the current directory
csv_directory = current_directory

# Define the output directory where the generated HTML pages will be saved
output_directory = os.path.join(current_directory, "product_pages")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Read the CSS styles from the style.css file
with open("style.css", "r") as css_file:
    css_styles = css_file.read()

# Loop through the CSV files in the directory
for file_name in os.listdir(csv_directory):
    if file_name.endswith(".csv"):
        file_path = os.path.join(csv_directory, file_name)

        # Open the CSV file for reading
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file)

            # Read the contents of the CSV file
            csv_contents = list(reader)

            # Extract the product name from the CSV contents
            product_name = csv_contents[1][3]  # Assuming the product name is in the 2nd row, 4th column

            # Create the HTML content for the product page
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Products - My Affiliate Marketing Website</title>
                <style>{css_styles}</style>
            </head>
            <body>
                <header>
                    <h1>Our Products</h1>
              <br />
      <nav>
        
                      <ul>
                        <li><a href="../index.html">Home</a></li>|
                        <li><a href="../products.html">Products</a></li>|
                        <li><a href="../contact.html">Contact</a></li>
                      </ul>
                    </nav>
                </header>
                <main>
                    <h2>{product_name}</h2>
                    <nav>
            """

            # Loop through the rows in the CSV file
            for row in csv_contents[1:]:
                link_code = row[0]
                advertiser = row[1]
                link_type = row[2]
                link_name = row[3]
                link_id = row[6]

                # Create the product HTML content using the link code and advertiser
                product_html = f'<a href="{link_code}"><img border="0" alt="{advertiser}" src="{link_name}"></a>'

                # Add the product HTML to the HTML content
                html_content += product_html

            # Add the closing tags to the HTML content
            html_content += """
                    </nav>
                </main>
                <footer>
                    <p>© 2023 My Affiliate Marketing Website</p>
                </footer>
            </body>
            </html>
            """

            # Generate the output file path for the product page
            output_file_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}.html")

            # Save the generated HTML content to the output file
            with open(output_file_path, "w") as output_file:
                output_file.write(html_content)

print("Product pages generated successfully.")
