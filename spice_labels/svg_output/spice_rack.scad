include <ScadStoicheia/centerable.scad>
include <ScadApotheka/material_colors.scad>



VISUALIZE = 0 + 0;
CUT = 1 + 0;
SCORE = 2 + 0;
LIGHT_ETCH = 3 + 0;
MEDIUM_ETCH = 4 + 0;
HEAVY_ETCH = 5 + 0;


mode = "3d"; // [3d, Cut, Score, Light, Medium, Heavy]
render_svg =  mode != "3d";

current_action = 
    mode == "3d" ? VISUALIZE :
    mode == "Cut" ? CUT :
    mode == "Score" ? SCORE :
    mode == "Light" ? LIGHT_ETCH :
    mode == "Medium" ? MEDIUM_ETCH :
    mode == "Heavy" ? HEAVY_ETCH : 
    assert(false);

module end_of_customization() {}

baltic_birch_one_eighth = [["z", 3.3], ["material", "baltic birch"]]; 

module colorize(color_name) {
    if (is_undef(color_name)) {
        children();
    } else {
        color(color_name) children();
    }
}


module lc_slab(laser_action, x, y, center=CENTER, part="Red", material=baltic_birch_one_eighth) {
    echo("material", material);
    if (render_svg && laser_action == current_action) {
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


module base() {
    lc_slab(CUT, 18, 18, CENTER, PART_1);
    lc_slab(SCORE, 16, 16, CENTER, PART_2);
    lc_slab(LIGHT_ETCH, 14, 14, CENTER, PART_3);
    lc_slab(MEDIUM_ETCH, 12, 12, CENTER, PART_4);
    lc_slab(HEAVY_ETCH, 10, 10, CENTER, PART_5);
}

base();
//}