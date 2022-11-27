# Readme for clothes labelling

For the annotation part in our project we use Label Studio.

To use label studio you should do the following steps:
 1. register for the Label Studio Community Edition
 2. `pip install label-studio`
 3. `label-studio start`
 4. Sign up
 5. Create a project
 6. Import the data
 7. Import **your part** of images
 8. Choose **Semantic Segmentation with Masks** as a labelling setup
 9. Switch to code view

    		Insert the following lines:
    		<View>
		      <Image name="image" value="$image" zoom="true"/>
		      <BrushLabels name="tag" toName="image">
			<Label value="Shirts" background="#FFA39E"/>
			<Label value="T-shirts" background="#D4380D"/>
			<Label value="Long-sleeves" background="#FFC069"/>
			<Label value="Jacket" background="#AD8B00"/>
			<Label value="Trousers" background="#D3F261"/>
			<Label value="Shorts" background="#389E0D"/>
			<Label value="Flip-flops" background="#5CDBD3"/>
			<Label value="Shoes" background="#096DD9"/>
			<Label value="Bikini" background="#ADC6FF"/>
			<Label value="Swimming-trunks" background="#9254DE"/>
			<Label value="Sun-glasses" background="#F759AB"/>
		     </BrushLabels>
		 </View> 
11. Save the project
10. Start  labelling

  
 
