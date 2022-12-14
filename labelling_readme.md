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
 10. Insert the following lines:
 11. `<View>
  	<Image name="image" value="$image"/>
  	<Choices name="choice" toName="image">
		<Choice value="None"/>
		<Choice value="jeans_tapered"/>
		<Choice value="jeans_wide"/>
		<Choice value="cargo_pants"/>
		<Choice value="suit_pants_tapered"/>
		<Choice value="suit_pants_wide"/>
		<Choice value="sweat_pants"/>
		<Choice value="track_pants"/>
		<Choice value="curdoroy_pants"/>
		<Choice value="micro_skirts"/>
		<Choice value="midi_skirts"/>
		<Choice value="maxi_skirts"/>
		<Choice value="stockings"/>
		<Choice value="leg_warmers"/>
		<Choice value="shorts"/>
		<Choice value="mid_length_shorts"/>
		<Choice value="denim_shorts"/>
		<Choice value="denim_skirts"/>
		<Choice value="linen_pants"/>
		<Choice value="cargo_skirt"/>
	</Choices>
</View>`
 11. Save the project
 12. Start  labelling

  
 
