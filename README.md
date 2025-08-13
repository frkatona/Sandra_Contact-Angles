# Contact Angle Analysis

![contact angles](contactangle.png)

Note that the angles are 180 - measured angle.  This is because the ImageJ plugin measures the angle between the tangent to the drop and the baseline because it assumes the drop is upside down, which it is not in our images.

## File Structure
- `contactangles.py`: analysis and plotting script
- `contactAngles.csv`: input data (tab-delimited)
- `raw-images/`: folder containing original images
- `processed-images/`: folder containing processed images and angle overlays

## Resources
 - Marco Brugnara's plugin .jar file: https://imagej.net/ij/plugins/contact-angle.html
 - ChemEd paper with a bunch of references: https://pubs.acs.org/doi/full/10.1021/ed100468u
 - Stora Enso example paper: https://www.storaenso.com/-/media/documents/download-center/documents/product-specifications/paperboard-materials/cupforma-natura-pe-15-us.pdf