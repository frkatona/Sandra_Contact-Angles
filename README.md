# Contact Angle Analysis Script

This repository contains a Python script (`contactangles.py`) for analyzing and visualizing contact angle measurements from image data. The script reads a CSV file with measurement results, computes summary statistics, performs statistical significance testing, and generates a bar plot with error bars and significance annotations.

Data was acquired using Marco Brugnara's ImageJ plugin, "Contact Angle" (https://imagej.net/ij/plugins/contact-angle.html).

## Dependencies

Install dependencies with:
```sh
pip install pandas numpy matplotlib scipy
```

## File Structure
- `contactangles.py`: analysis and plotting script
- `contactAngles.csv`: input data (tab-delimited)
- `raw-images/`: folder containing original images
- `processed-images/`: folder containing processed images and angle overlays