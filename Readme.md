<h3>Image Pre-Processing</h3>
<ul>
    <li>
    Capture two images, that will be used for processing, (one underexposed, and one
    overexposed)
    <ul>
        <li>Apply the gamma transformation to these two gray level images to correct their
            appearance.
        </li>
        <li>Test several parameters of gamma until obtaining the best results and plot the
            histograms of both original and corrected images.
        </li>
    </ul>
    <h5>Result: </h5>
        <h6>Over Exposed Result: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/image-gamma-transformation/gamma_transposed_overexpose.jpg"
        alt="Over Exposed Plot"
        style="float: left; margin-right: 10px;" />
        <h6>Under Exposed Result: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/image-gamma-transformation/gamma_transposed_underexpose.jpg"
        alt="Over Exposed Plot"
        style="float: left; margin-right: 10px;" />    
    </li>
    <li>
    Apply Histogram equalization to the Over exposed and under exposed image.
    <h5>Result: </h5>
        <h6>Over Exposed Result: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/histogram-equalization/overexposed_img_hist_eql.jpg"
        alt="Over Exposed Plot"
        style="float: left; margin-right: 10px;" />
        <h6>Under Exposed Result: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/histogram-equalization/underexposed_img_hist_eql.jpg"
        alt="Over Exposed Plot"
        style="float: left; margin-right: 10px;" />    
    </li>
    <li>
     Improve Image contrast using Exact Histogram Matching.
     <h5>Result</h5>
        <h6>Source Image: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/ImageData/kernel_overexpose.jpg"
        alt="Source Image"
        style="float: left; margin-right: 10px;" />
        <h6>Reference Image: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/ImageData/kernel_underexpose.jpg"
        alt="Reference Image"
        style="float: left; margin-right: 10px;" /> 
        <h6>Grayscale Image: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/histogram-matching-using-kernel/image.jpg"
        alt="Grayscale Image To apply the kernel"
        style="float: left; margin-right: 10px;" />
        <h6>Exact Histogram Match Image: </h6>
        <img src="https://github.com/Arx1971/Image-Pre-Processing/blob/master/histogram-matching-using-kernel/histogram_matching_image.jpg"
        alt="Output Image"
        style="float: left; margin-right: 10px;" />
    </li>
</ul>