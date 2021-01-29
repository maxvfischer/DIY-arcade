![main gif](./images/main_gif.gif)

This guide goes through all the steps necessary to build your own full-size arcade machine, including the 
pre-designed CAD-files, how to assemble all the cabinet parts, how to set up the Raspberry Pi running the arcade program
etc. The project was my first project going from CAD to actual build (actually also the first time I used a CAD 
program).

If you have any questions, feel free to contact me on LinkedIn: [https://www.linkedin.com/in/max-fischer-92997281/
](https://www.linkedin.com/in/max-fischer-92997281/
)

## Table of content
1. [Build the cabinet](#build-the-cabinet)
    1. [Download the CAD-file](#download-the-cad-file)
    2. [CNC parts](#cnc-parts)
    3. [Hand-cut parts](#hand-cut-parts)
    4. [Draw outlines of parts](#draw-outlines-of-parts)
    5. [Cut wood biscuits holes](#cut-wood-biscuits-holes)
    6. [Glue main parts together](#glue-main-parts-together)
    7. [Adding cabinet legs](#adding-cabinet-legs)
    8. [Add screen panel](#add-screen-panel)
    9. [Preparing the light box](#preparing-the-light-box)
    10. [Spackling paste and sanding](#spackling-paste-and-sanding)
    11. [Spray painting](#spray-painting)
    12. [Art work](#art-work)
    
2. [Add electronics](#add-electronics)
    1. [Add electricity to the cabinet](#add-electricity-to-the-cabinet)
    2. [Screen](#screen)
    3. [Light box](#light-box)
    4. [Arcade buttons and joystick](#arcade-buttons-and-joystick)
    5. [Set up RetroPie on Raspberry Pi](#set-up-retropie-on-raspberry-pi)
    6. [Configure arcade buttons and joysticks](#configure-arcade-buttons-and-joysticks)
    7. [Power button](#power-button)
    8. [Speakers](#speakers)
    9. [Structure cables](#structure-cables)

3. [Final arcade machine](#final-arcade-machine)
    1. [Contact](#contact)

## Build the cabinet

### Download the CAD-file
The CAD design was created in AutoCAD Fusion 360. This was my first experience using any CAD-program, so the design 
is likely far from optimal and there are probably a lot of possibilities for improvements. Note that all the CAD-files are in millimeters.
 
[Watch the CAD-file on GitHub's 3D File Viewer](./cad_files/arcade_cabinet.stl)
 
[Download .dwg CAD-file](./cad_files/arcade_cabinet.dwg)

[Download .obj CAD-file](./cad_files/arcade_cabinet.obj)

[Download .step CAD-file](./cad_files/arcade_cabinet.step)

[Download .stl CAD-file](./cad_files/arcade_cabinet.stl)

![fly around arcade](./images/build/CAD_fly_around.gif)

### CNC parts
To get a perfect fit for the arcade buttons and joysticks, the screen, the power button and the speakers, the 
_button panel_ and the _screen panel_ were CNC-cut. This was more expensive than doing it by hand, but lead to a much 
better finish. To make the cabinet fit perfectly together, the two side panels were also CNC cut, as they have multiple 
rounded shapes that need to be identical on both sides.

![screen panel](./images/build/screen_panel.jpg)

![button panel](./images/build/button_panel.jpg)

![side panel](./images/build/side_panel.jpg)

![all cnc parts](./images/build/all_cnc_parts.jpg)

Oh, and remember to CNC-cut the CAD file on size 1:1 and not "utilize full MDF board"... ¯\\_(ツ)_/¯

![wrong cnc](./images/build/wrong_cnc.jpg)

### Hand-cut parts
As the rest of the parts were more or less rectangular, they were cut by "hand". To do this, two different mounted saws
were used:
* A vertical panel saw to cut down the MDF to smaller pieces
* A table saw to cut out the final pieces

![vertical panel saw](./images/build/vertical_panel_saw.jpg)

![vertical panel saw](./images/build/table_saw.jpg)

| Piece              | Image                                                              |
|--------------------|--------------------------------------------------------------------|
| Back panel         | ![vertical panel saw](./images/build/back_panel_table.jpg)         |
| Bottom panel       | ![vertical panel saw](./images/build/bottom_panel_table.jpg)       |                                                |
| Below button panel | ![vertical panel saw](./images/build/below_button_panel_table.jpg) |                                                 |
| Hatch panel        | ![vertical panel saw](./images/build/hatch_panel_table.jpg)        |                                         |
| Light box panel 1  | Missing                                                            |
| Light box panel 2  | ![vertical panel saw](./images/build/light_box_panel_2_table.jpg)  |                                               | 

The only panel that needed some more work was the hatch panel. The outlines of the hatch were first sketched on the 
panel.

![hatch 1](./images/build/hatch_1.jpg)

A circle saw was then used to cut out the actual hatch.

![hatch 2](./images/build/hatch_2.jpg)

![hatch 3](./images/build/hatch_3.jpg)

A hand held jigsaw was used for the edges as it's difficult to know how far the circle saw will cut.

![hatch 4](./images/build/hatch_4.jpg)

After the main part was separated into the inner and outer part, "blockers" were glued and nailed into place. This, 
together with a standard window magnet was used to keep the hatch in place.

A hole was also cut at the top of the inner part to enable it to be opened.

![hatch 5](./images/build/hatch_5.jpg)

![hatch 12](./images/build/hatch_12.jpg)

![hatch 6](./images/build/hatch_6.jpg)

![hatch 14](./images/build/hatch_14.jpg)

![hatch 7](./images/build/hatch_7.jpg)

![hatch 8](./images/build/hatch_8.jpg)

![hatch 9](./images/build/hatch_9.jpg)

![hatch 13](./images/build/hatch_13.jpg)

![hatch 10](./images/build/hatch_10.jpg)

![hatch 11](./images/build/hatch_11.jpg)

A hole was also drilled at the bottom of the large back panel to prepare for a power strip to be inserted.

![cable grommet 1](./images/build/electricity_grommet_1.jpg)

![cable grommet 2](./images/build/electricity_grommet_2.jpg)

### Draw outlines of parts
It was important to fixate all the parts at the same location on both side panels for the cabinet to be symmetrical. To 
simplify this, outlines were drawn where each panel was supposed to be attached to the side panels. As the button panel 
and the screen panel were attached at an angle, their outlines were first drawn on one of the side panels. Then the 
outlines were reflected and transferred to the other side panel by using some reference points. It was a bit tricky, 
so take your time.

![vertical panel saw](./images/build/outlines_side_panel_2.jpg)

![vertical panel saw](./images/build/outlines_side_panel_3.jpg)

![vertical panel saw](./images/build/outlines_side_panel_4.jpg)

![vertical panel saw](./images/build/outlines_side_panel_5.jpg)

![vertical panel saw](./images/build/outlines_side_panel_6.jpg)

![vertical panel saw](./images/build/outlines_side_panel_7.jpg)

![vertical panel saw](./images/build/outlines_side_panel_8.jpg)

![vertical panel saw](./images/build/outlines_side_panel_9.jpg)

![vertical panel saw](./images/build/outlines_side_panel_10.jpg)

![vertical panel saw](./images/build/outlines_side_panel_11.jpg)

### Cut wood biscuits holes
To hold all the panels together, wood biscuits, wood glue and a nail gun were used. The wood biscuits are not only good 
for making the cabinet robust, but they also help with fixating all the panels at the right places and angles. The only 
panel that wasn't attached with wood biscuits was the screen panel. The reason was for the screen to be interchangeable 
if it breaks, something that is not possible (or atleast very difficult) if the panel is glued in place.

When using the wood biscuit cutter, it's important that the holes end up at the correct place at the aligning panels. 
One simple way of solving this is to align your panels and then draw a line on both panels at the center of where you 
want the biscuit to be. If you do this, the holes will end up at the right place.

![vertical panel saw](./images/build/biscuit_joiner_2.jpg)

![vertical panel saw](./images/build/biscuit_joiner_5.jpg)

![vertical panel saw](./images/build/biscuit_joiner_6.jpg)

![vertical panel saw](./images/build/biscuit_joiner_1.jpg)

![vertical panel saw](./images/build/biscuit_joiner_3.jpg)

![vertical panel saw](./images/build/biscuit_joiner_4.jpg)

Before gluing all the parts together, make sure that they fit by placing each panel at their place. A tip is to draw
shapes (triangles, circles etc) on connecting parts, so you easily know which parts that go together later on.

![vertical panel saw](./images/build/fit_panels_1.jpg)

![vertical panel saw](./images/build/fit_panels_2.jpg)

![vertical panel saw](./images/build/fit_panels_3.jpg)

### Glue main parts together
When gluing the parts together, you'll need to be fairly quick and structured. I started of by laying down one side 
panel first, then gluing the middle parts and finally gluing the other side panel.

Start of by adding the glue in the wood biscuit holes. Then press down the wood biscuits into the holes. After that you 
apply wood glue along all the connecting parts and press them together.

![glue 2](./images/build/glue_2.jpg)

![glue 3](./images/build/glue_3.jpg)

![glue 4](./images/build/glue_4.jpg)

![glue 5](./images/build/glue_5.jpg)

![glue 1](./images/build/glue_1.jpg)

When done, make sure that all the parts are aligned and in the right position. Then apply force using large clamps and 
nail everything together using a nail gun.

![glue 6](./images/build/glue_6.jpg)

![glue 7](./images/build/glue_7.jpg)

![glue 8](./images/build/glue_8.jpg)

Also, don't forget to remove redundant glue dripping out from the connecting parts, it makes it much easier to get a 
nice finish later on.

![glue 9](./images/build/glue_9.jpg)

### Adding cabinet legs
To distribute the upwards force from the legs, a small block of wood was glued and nailed in each corner inside the 
cabinet.

![legs 5](./images/build/legs_5.jpg)

I had some wood laying around that I used as legs for the cabinet. After cutting out four squares, make sure that they 
fit nicely in each corner.

![legs 1](./images/build/legs_1.jpg)

Use a sand paper to round the edges.

![legs 2](./images/build/legs_2.jpg)

The legs was then glued from the outside and screwed from the inside.

![legs 3](./images/build/legs_3.jpg)

![legs 4](./images/build/legs_4.jpg)

### Add screen panel
To be able to easily remove and change the screen, the screen panel was screwed in place. Two slim wood bars were
glued and nailed on each inner side at the correct angle for the screen panel to rest on.

![screen panel 1](./images/build/screen_panel_1.jpg)

![screen panel 2](./images/build/screen_panel_2.jpg)

![screen panel 4](./images/build/screen_panel_4.jpg)

![screen panel 3](./images/build/screen_panel_3.jpg)

To get a nice seamless look of the screen, a handheld milling machine was used to extract a slot for the screen on the
back side of the screen panel.

![screen panel 5](./images/build/screen_panel_5.jpg)

![screen panel 6](./images/build/screen_panel_6.jpg)

![screen panel 7](./images/build/screen_panel_7.jpg)

![screen panel 8](./images/build/screen_panel_8.jpg)

![screen panel 9](./images/build/screen_panel_9.jpg)

The screen I used had button on the front, so I needed to drill holes in the screen panel for them to be clickable.

![screen panel 10](./images/build/screen_panel_10.jpg)

![screen panel 11](./images/build/screen_panel_11.jpg)

![screen panel 12](./images/build/screen_panel_12.jpg)

![screen panel 13](./images/build/screen_panel_13.jpg)

Finally, the screw keeping the screen panel in place were aligned with the speakers to get a nice look.

![screen panel 14](./images/build/screen_panel_14.jpg)

### Preparing the light box
As a true retro arcade cabinet, of course we need a glowing light box at the top of the cabinet. To keep the plexiglass
in place, four small wood cubes were glued and nailed at each corner for the plexiglass to rest on.

![preparing lightbox 1](./images/build/preparing_lightbox_1.jpg)

![preparing lightbox 2](./images/build/preparing_lightbox_2.jpg)

### Spackling paste and sanding
Before the cabinet was sent to spray painting, final touches were made to get a nice smooth finish. Spackling paste 
was applied to cover up all the nails and plastic padding was used to cover up small visible mistakes made. When 
everything had dried, an electric sander was used to remove redundant spackling paste and plastic padding. All the edges
was smoothed by manual sanding.

![spackling paste 1](./images/build/spackling_paste_1.jpg)

![spackling paste 2](./images/build/spackling_paste_2.jpg)

![spackling paste 3](./images/build/spackling_paste_3.jpg)

![spackling paste 4](./images/build/spackling_paste_4.jpg)

![spackling paste 5](./images/build/spackling_paste_5.jpg)

![spackling paste 6](./images/build/spackling_paste_6.jpg)

![spackling paste 7](./images/build/spackling_paste_7.jpg)

![spackling paste 8](./images/build/spackling_paste_8.jpg)

### Spray painting
To get a nice finish, I payed a professional to spray paint the cabinet in a black lacquer color. To get a good
light reflection in the light box, I got it painted white.

![spray painted 1](./images/build/spray_painted_1.jpg)

![spackling paste 8](./images/build/spray_painted_2.jpg)

![spackling paste 8](./images/build/spray_painted_3.jpg)

![spackling paste 8](./images/build/spray_painted_4.jpg)

### Art work
I'm familiar with Adobe Illustrator, but far from an expert in creating art work. So to create the art work, I paid for 
a premium subscription at Freepik (https://www.freepik.com) that costs 9.99 €/month. This enabled me to download a bunch 
of different high-quality vectorized retro illustrations that I combined into the final art work. When done, I printed them 
as stickers.

![art work 1](./images/build/art_work_1.gif)

![art work 2](./images/build/art_work_2.jpg)

A good way to apply the art work is to tape the sticker at one side to fixate it, then you remove some of the
cover and start scraping it from the bottom up. By doing so, you'll get it at the exact position while reducing the 
number of bubbles.

![art work 3](./images/build/art_work_3.jpg)

![art work 4](./images/build/art_work_4.jpg)

![art work 5](./images/build/art_work_5.jpg)

![art work 6](./images/build/art_work_6.jpg)

![art work 7](./images/build/art_work_7.jpg)

![art work 8](./images/build/art_work_8.jpg)

![art work 9](./images/build/art_work_9.jpg)

![art work 10](./images/build/art_work_10.jpg)

![art work 11](./images/build/art_work_11.jpg)

![art work 12](./images/build/art_work_12.jpg)

The side stickers were so large that they had to be split into two separate parts. To keep the correct alignment, 
arrows were drawn indicating where the two parts should align. A small space were kept at the bottom to reduce the risk 
of the sticker being peeled off. 

![art work 13](./images/build/art_work_13.jpg)

![art work 14](./images/build/art_work_14.jpg)

![art work 15](./images/build/art_work_15.jpg)

![art work 16](./images/build/art_work_16.jpg)

![art work 17](./images/build/art_work_17.jpg)

Stickers indicating the button configuration were also added.

![art work 19](./images/build/art_work_19.jpg)

![art work 20](./images/build/art_work_20.jpg)

![art work 18](./images/build/art_work_18.jpg)

## Add electronics

### Add electricity to the cabinet
A round plastic cable grommet was inserted into the hole previously drilled at the bottom of the back panel. A 
power strip was then added.

![power strip 1](./images/build/power_strip_1.jpg)

![power strip 2](./images/build/power_strip_2.jpg)

### Screen

The screen was kept in place by using galvanized banding straps.

![screen 1](./images/build/screen_1.jpg)

![screen 2](./images/build/screen_2.jpg)

![screen 3](./images/build/screen_3.jpg)

![screen 4](./images/build/screen_4.jpg)

![screen 5](./images/build/screen_5.jpg)

### Light box
To get a consistent feel of the art work I reused some of the graphical component from the side panels.

![light box 1](./images/build/light_box_1.jpg)

The art work was printed as one large sticker and the text "ARCADE MACHINE" was cut out to let the light through. The 
sticker was then attached to a frosted plexiglas.

![light box 2](./images/build/light_box_2.jpg)

For the light source I used a LED tube of fitting length, with a wire that was long enough to go all the way 
down to the power strip at the bottom of the cabinet. The LED tube was attached to the back panel by using 
double-coated adhesive tape.

![light box 3](./images/build/light_box_3.jpg)

![light box 4](./images/build/light_box_4.jpg)

![light box 5](./images/build/light_box_5.jpg)

![light box 6](./images/build/light_box_6.jpg)

To remove potential light leakage around the plexiglas, long stripes of foam was cut and attached behind the plexiglas
edges using double-coated adhesive tape.

![light box 8](./images/build/light_box_8.jpg)

![light box 9](./images/build/light_box_9.jpg)

![light box 10](./images/build/light_box_10.jpg)

![light box 11](./images/build/light_box_11.jpg)

![light box 12](./images/build/light_box_12.jpg)

![light box 13](./images/build/light_box_13.jpg)

![light box 14](./images/build/light_box_14.jpg)

Double-coated adhesive tape was also used to keep the plexiglas in place.

![light box 15](./images/build/light_box_15.jpg)

![light box 16](./images/build/light_box_16.jpg)

![light box 17](./images/build/light_box_17.jpg)

### Arcade buttons and joysticks

Before I started this project, I bought two sets of arcade buttons and joysticks from Aliexpress. This type of button set is very 
convenient to use, even without any knowledge of electronic circuit boards. I don't know if this exact set is still 
available, but I've seen multiple vendors selling similar types of arcade button sets.

Using this type of set makes hooking up the buttons very simple. You attach each button and the joystick to the circuit
board that is included in the set. Then you connect the USB-cord to the circuit board and to the computer.

![arcade_buttons 1](./images/build/arcade_buttons_1.jpg)

![arcade_buttons 2](./images/build/arcade_buttons_2.jpg)

To center the joysticks in the holes, I used a wide double-coated adhesive tape normally used to attach rugs to 
floors. It's easier to be two people doing this, one person centering the joystick from the top, while the other person 
locking it in place. The joysticks were then screwed into the button panel. 

![arcade_buttons 4](./images/build/arcade_buttons_4.jpg)

![arcade_buttons 5](./images/build/arcade_buttons_5.jpg)

![arcade_buttons 3](./images/build/arcade_buttons_3.jpg)

![arcade_buttons 6](./images/build/arcade_buttons_6.jpg)

![arcade_buttons 8](./images/build/arcade_buttons_8.jpg)

![arcade_buttons 7](./images/build/arcade_buttons_7.jpg)

### Set up RetroPie on Raspberry Pi
RetroPie (https://retropie.org.uk/) is the program that enables you to create a retro gaming station out of the 
Raspberry Pi. As RetroPie is an open-source project that is continuously updated, it's easiest for you to follow the 
installation guide on their website: https://retropie.org.uk/docs/First-Installation/ (visited at 2020-09-06).

### Configure arcade buttons and joysticks
The USB cables from the arcade button electronic circuit boards were connected to the Raspberry Pi.
When the Raspberry Pi is turned on and RetroPie is started, a welcome screen should be visible, asking you to configure 
the controllers.

### Power button
To enable a convenient way of shutting down the arcade machine, I added a hole in the screen panel,
fitting a power button.

![power button 1](./images/build/power_button_1.jpg)

Two cables were then soldered to the button and attached to the GPIO pins 5 and 6 on the Raspberry Pi (see a 
GPIO diagram here: https://www.raspberrypi.org/documentation/usage/gpio/, visited 2020-09-06). When shortening the 
GPIO pins 5 and 6, the Raspberry Pi is natively waken up from its halted state.

![power button 2](./images/build/power_button_2.jpg)

![power button 3](./images/build/power_button_3.jpg)

![power button 4](./images/build/power_button_4.jpg)

![power button 5](./images/build/power_button_5.jpg)

A small script was then added and executed on start up of the Raspberry Pi. The script listened to another shortening of
the GPIO pins 5 and 6, that then triggered a safe shutdown of the machine.

To add the shutdown script, do the following:
1. Start the Raspberry Pi
2. When the EmulationStation (RetroPie) has started, click F4 on your keyboard to enter bash
3. Make sure that you have python and pip installed
4. Install RPi.GPIO: `pip install RPi.GPIO` (see https://pypi.org/project/RPi.GPIO/)
5. Create a utils folder under /home: `mkdir /home/utils/`
6. Add [this script (shutdown_script.py)](./scripts/shutdown_script.py) to the newly created utils folder
7. To make the Raspberry run this script on start up, add the line `python3 /home/utils/shutdown_script.py &` at the 
end of the file `/etc/rc.local`, just before `exit 0`

![power button 6](./images/build/power_button_6.gif)

As of now, the power button only shuts down the Raspberry Pi. In the future, I would like to add a relay controlled by 
the Raspberry Pi, turning of all the other electronics as well (screen, light box etc).

### Speakers
Two speaker wires were soldered to each speaker. The speakers were then placed in the CNC-cut holes and attached by 
screws to the screen panel. All cables were then connected to the amplifier. A 3.5mm AUX stereo cable was then
connected between the amplifier and the Raspberry Pi.

![speakers 1](./images/build/speakers_1.jpg)

![speakers 2](./images/build/speakers_2.jpg)

![speakers 3](./images/build/speakers_3.jpg)

![speakers 4](./images/build/speakers_4.jpg)

### Structure cables
To keep everything nice and structured inside the cabinet, I attached cable canals with double-coated adhesive tape.

![structure cables 1](./images/build/structure_cables_1.jpg)

![structure cables 2](./images/build/structure_cables_2.jpg)

![structure_cables 3](./images/build/structure_cables_3.jpg)

![structure cables 4](./images/build/structure_cables_4.jpg)

![structure cables 5](./images/build/structure_cables_5.jpg)

![structure cables 6](./images/build/structure_cables_6.jpg)

![structure cables 7](./images/build/structure_cables_7.jpg)

## Final arcade machine
![final arcade](./images/build/final_arcade.gif)

![final arcade 1](./images/build/final_arcade_1.jpg)

![final arcade 2](./images/build/final_arcade_2.jpg)

![final arcade 3](./images/build/final_arcade_3.jpg)

### Contact
If you have any questions, feel free to contact me:

![contact](./images/contact.png)