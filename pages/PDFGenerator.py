from fpdf import FPDF
import pandas as pd
import streamlit as st
import base64


# Define function to generate PDF
def generate_pdf(df):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    for index, row in df.iterrows():
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)

        # Set Footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

        for i in range(row["Pages"] - 1):
            pdf.add_page()
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    return pdf


# Streamlit app
def main():
    st.title("PDF Generator")

    uploaded_file = st.file_uploader("Upload CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Check if the required columns are present
        if "Order" in df.columns and "Topic" in df.columns and "Pages" in df.columns:
            st.write("CSV file uploaded successfully.")
            st.write(df)

            # Generate PDF
            pdf = generate_pdf(df)
            pdf_bytes = pdf.output(dest='S').encode('latin1')
            b64_pdf = base64.b64encode(pdf_bytes).decode()

            # Create download link
            href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="output.pdf">Download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

            st.success("PDF generated successfully.")
        else:
            st.error("CSV file should contain columns: 'Order', 'Topic', and 'Pages'.")


if __name__ == "__main__":
    main()
