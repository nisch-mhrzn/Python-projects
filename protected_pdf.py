import pikepdf

old_pdf = pikepdf.Pdf.open("certificate.pdf")

no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("pro_new.pdf", encryption=pikepdf.Encryption(user="123asd",owner="Nisch",allow=no_extr
                                                          ))

