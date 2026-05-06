import streamlit as st
import qrcode
from PIL import Image

# Page title
st.title("QR Code Generator")

# User input
data = st.text_input("Enter URL")

# Generate button
if st.button("Generate QR"):

    if data:

        # Generate QR code
        qr = qrcode.make(data)

        # Save QR image
        qr.save("qr.png")

        # Open image
        img = Image.open("qr.png")

        # Display image
        st.image(img, caption="Generated QR Code")

        # Download button
        with open("qr.png", "rb") as f:
            st.download_button(
                "Download QR",
                f,
                file_name="qr.png",
                mime="image/png"
            )

    else:
        st.warning("Please enter some text")
