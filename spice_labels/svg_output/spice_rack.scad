include <ScadStoicheia/centerable.scad>
include <ScadStoicheia/not_included_batteries.scad>
include <ScadApotheka/material_colors.scad>



VISUALIZE = 0 + 0;
LAYOUT =  1 + 0;
CUT = 2 + 0;
SCORE = 3 + 0;
LIGHT_ETCH = 4 + 0;
MEDIUM_ETCH =5 + 0;
HEAVY_ETCH = 6 + 0;




mode = "3d"; // [3d, 2d, Cut, Score, Light, Medium, Heavy]
render_svg =  mode != "3d";

current_action = 
    mode == "3d" ? VISUALIZE :
    mode == "2d" ? LAYOUT :
    mode == "Cut" ? CUT :
    mode == "Score" ? SCORE :
    mode == "Light" ? LIGHT_ETCH :
    mode == "Medium" ? MEDIUM_ETCH :
    mode == "Heavy" ? HEAVY_ETCH : 
    assert(false);
    
x_part_1 = 10; // [0:200]
x_part_2 = 20; // [0:200]
x_part_3 = 30; // [0:200]
x_part_4 = 40; // [0:200]
x_part_5 = 50; // [0:200]
x_part_6 = 60; // [0:200]

y_part_1 = 10; // [0:200]
y_part_2 = 20; // [0:200]
y_part_3 = 30; // [0:200]
y_part_4 = 40; // [0:200]
y_part_5 = 50; // [0:200]
y_part_6 = 60; // [0:200]

module end_of_customization() {}


svg_layout = [
    [PART_1, [x_part_1, y_part_1, 0]],
    [PART_2, [x_part_2, y_part_2, 0]],
    [PART_3, [x_part_3, y_part_3, 0]],
    [PART_4, [x_part_4, y_part_4, 0]],
    [PART_5, [x_part_5, y_part_5, 0]],
    [PART_6, [x_part_5, y_part_5, 0]],  
];

baltic_birch_one_eighth = [["z", 3.3], ["material", "baltic birch"]]; 

module colorize(color_name) {
    if (is_undef(color_name)) {
        children();
    } else {
        color(color_name) children();
    }
}

module lc_translate(part, three_d_translation) {
    if(render_svg) {
        two_d_translation = find_in_dct(svg_layout, part);
        if (is_undef(two_d_translation)) {
            echo("Warning: No 2d translation was found for part ", part);
            children();
        } else {
            translate(two_d_translation) children();
        }
    } else {
        translate(three_d_translation) children();
    }
}


module lc_slab(part, laser_action, x, y, center=CENTER, material=baltic_birch_one_eighth) {
    echo("material", material);
    if ((render_svg && laser_action == current_action) || (current_action == LAYOUT)) {
        colorize(part) square([x, y], center=true);
    } else if (current_action == VISUALIZE) {
        z = material[0][1]; 
        echo("z", z);
        extent = [x, y, z];
        
        colorize(part) {
            block(extent, center=center);
        }
    }
}


module lc_text(part, t, size=undef, font=undef, halign=undef, valign=undef, spacing=undef, laser_action=LIGHT_ETCH) {
    module generate_text() {
        text(t, size=size, font=font, halign=halign, valign=valign, spacing=spacing);
    }
    if ((render_svg && laser_action == current_action) || (current_action == LAYOUT)) {
        colorize(part) generate_text();
    } else if (current_action == VISUALIZE) { 
        colorize(part) linear_extrude(4) generate_text(); 
    }
} 



module base() {
    lc_translate(PART_1, [20, 20, 10]) lc_slab(PART_1, CUT, 18, 18, CENTER);
    lc_translate(PART_2, [30, 20, 20]) lc_slab(PART_2, SCORE, 16, 16, CENTER);
    lc_translate(PART_3, [40, 20, 30]) lc_slab(PART_3, LIGHT_ETCH, 14, 14, CENTER);
    lc_translate(PART_4, [50, 20, 40]) lc_slab(PART_4, MEDIUM_ETCH, 12, 12, CENTER);
    lc_translate(PART_5, [60, 20, 50]) lc_slab(PART_5, HEAVY_ETCH, 10, 10, CENTER);
    lc_translate(PART_6, [60, 20, 50]) lc_text(PART_6, "Cinnamon", laser_action=CUT);
    
}

base();
