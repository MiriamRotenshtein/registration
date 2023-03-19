# RGB Histogram Visualization

This project is a Python script that visualizes the RGB histogram of an image in 3D space. It uses the NumPy and Matplotlib libraries to process and plot the data, and the PIL library to read the image file.

## Getting Started

To run the script, you need to have Docker installed on your machine. Then, follow these steps:

   1. Clone this repository to your local machine.
   2. Open a terminal window and navigate to the repository's directory.
   3. Build the Docker image by running the following command:

```
docker build -t rgb-by-numpy .
```

  4. Run the Docker container by running the following command:

```
docker run rgb-by-numpy

```
  5. The script will run and display a 3D plot of the RGB histogram of the image `lightBlue`.png" located in the `images` folder.

## Customizing the Image

If you want to visualize the RGB histogram of a different image, replace the file `lightBlue`.png" in the `images` folder with your own image file, and then rebuild and run the Docker image.
