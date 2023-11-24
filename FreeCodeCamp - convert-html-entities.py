"""
Convert HTML Entities
Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a string to their corresponding HTML entities.

convertHTML("Dolce & Gabbana") should return the string Dolce &amp; Gabbana.
Waiting:convertHTML("Hamburgers < Pizza < Tacos") should return the string Hamburgers &lt; Pizza &lt; Tacos.
Waiting:convertHTML("Sixty > twelve") should return the string Sixty &gt; twelve.
Waiting:convertHTML('Stuff in "quotation marks"') should return the string Stuff in &quot;quotation marks&quot;.
Waiting:convertHTML("Schindler's List") should return the string Schindler&apos;s List.
Waiting:convertHTML("<>") should return the string &lt;&gt;.
Waiting:convertHTML("abc") should return the string abc.
"""

def convertHTML(str):
  html = {"&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&apos;",
          }
  for char, entity in html.items():
    if char in str:
      new_str = str.replace(char, entity)
      print(new_str)

convertHTML('Stuff in "quotation marks"')