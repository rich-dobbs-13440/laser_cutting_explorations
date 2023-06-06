include <ScadStoicheia/centerable.scad>
use <ScadStoicheia/visualization.scad>
include <ScadApotheka/material_colors.scad>
use <ScadApotheka/m2_helper.scad>
include <nutsnbolts-master/cyl_head_bolt.scad>
include <nutsnbolts-master/data-metric_cyl_head_bolts.scad>
use <PolyGear/PolyGear.scad>


a_lot = 200;
d_filament = 1.75 + 0.;
d_filament_with_clearance = d_filament + 0.75;  // Filament can be inserted even with elephant footing.
od_ptfe_tube = 4 + 0;
id_ptfe_tube = 2 + 0;
d_ptfe_insertion = od_ptfe_tube + 0.5;
d_m2_nut_driver = 6.0;

NEW_DEVELOPMENT = 0 + 0;
DESIGNING = 1 + 0;
MESHING_GEARS = 2 + 0;
ASSEMBLE_SUBCOMPONENTS = 3 + 0;
PRINTING = 4 + 0;



/* [Output Control] */

mode = 2; // [0:"New development, hide other parts", 1:"Designing, no rotation or translation", 2:"Meshing gears", 3: "assembly", 4: "Printing"]

// function layout_from_mode(mode) = 
//     mode == NEW_DEVELOPMENT ? "hidden" :
//     mode == DESIGNING ? "as_designed" :
//     mode == MESHING_GEARS ? "mesh_gears" :
//     mode == ASSEMBLE_SUBCOMPONENTS ? "assemble" :
//     mode == PRINTING ? "printing" :
//     "unknown";
    
show_parts = true;
show_vitamins = true;
show_filament = true;
show_drive_gear_construction_lines = false;
assert_for_not_implemented = false;
explode  = false;  
    
/* [Visibility] */

hub = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]
spokes = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]
clamp_gear  = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]
drive_gear = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]
drive_gear_retainer = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]
drive_shaft = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]
alt_drive_gear_retainer = 1; // [1:Solid, 0.25:Ghostly, 0:"Invisible, won't print" ]

include_drive_gear_spacer = true;
include_drive_shaft_side = true;
include_exit_side = false;
   
slide_length = 50; // [1 : 1 : 99.9]
screw_lift = 0; // [-.1 : .1 : 1]


/* [Clamp Gearing Design] */
module_clamp_gear = 1.2;
n_teeth_clamp_gear = 9; // [9, 10, 11, 12, 13]
cone_angle_clamp_gear = 5; // [-90:5:85]
tooth_width_clamp_gear = 6;
clamp_slide_clearance = 0.2;
range_of_rotation_clamp_gear = 720;

/* [Drive Gear_Retainer Design] */
l_shaft_screws = 12; // [8, 10, 12, 16, 20]
s_nut_cut = 5;
padding_drive_gear_retainer_shaft = 1;
d_drive_gear_retainer_shaft = ceil(d_filament_with_clearance + 2*s_nut_cut + padding_drive_gear_retainer_shaft);
echo("d_drive_gear_retainer_shaft", d_drive_gear_retainer_shaft);
clearance_drive_gear_retainer_shaft = 0.5;
// 1.25 is a kludge for working with currently printed items.
clearance_for_d_cap = 3; // [0.5, 1.25]
h_drive_gear_retainer_cap = 2;
h_spacer = h_drive_gear_retainer_cap + 1;
r_drive_shaft_screws = 10; // [10:0.1:12]
od_spacer = 2* r_drive_shaft_screws + 6;

/* [Drive Gearing Design] */
//The tooth width needs to be wide enough that the
// clamp bearing overlaps the slide, but it can't
// bee too wide or the the outer ptfe won't engage the
// the outer bearing

tooth_width_drive_gear = 6;
cone_angle_drive_gear = 90 - cone_angle_clamp_gear;
module_drive_gear = module_clamp_gear;
h_base_drive_gear = 2; 

m2_head_allowance = 6;
d_inner_hub_drive_gear = d_drive_gear_retainer_shaft + 2*m2_head_allowance;


/* [Slide Design] */
s_nut_block = 5;
l_slide_screws = 20; // [8, 10, 12, 16, 20]
// Make it big enough that the overlaps the drive gear id so it will extend into the clamp gear
h_inner_ptfe_bearing = 5;
clamping = 0.2;
dx_clamp_screw = d_filament/2 - clamping + screw_lift;


/* [Hub Design] */
r_hub = 9;
h_hub = s_nut_block;
r_nut_cut_clamp_screw = 4;
r_hub_attachment_screw = 3;

y_spoke_base = 7; // [0:10]

/* [Drive Shaft Design] */
gear_height_shaft = 50;
gear_module_shaft = 0.8;
n_teeth_shaft = 9;
od_flange = od_spacer;



/* [Build Plate Layout] */

dx_hub_bp  = -13; // [-100: 100]
dy_hub_bp  = 30; // [-100: 100]

dx_clamp_gear_bp = 12; // [-100: 100]
dy_clamp_gear_bp = -18; // [-100: 100]

dx_drive_gear_bp = 25; // [-100: 100]
dy_drive_gear_bp = 10; // [-100: 100]

dx_drive_shaft_bp = 0; // [-100: 100]
dy_drive_shaft_bp = -15; // [-100: 100]

dx_drive_gear_retainer = -25;  // [-100: 100]
dy_drive_gear_retainer = 10;  // [-100: 100]

module end_of_customization() {}



/* Visualization  */ 

layout = layout_from_mode(mode);
//echo("mode", mode, "layout", layout);

visualization_hub = 
    visualize_info(
        "Hub", PART_1, hub, layout, show_parts); 

visualization_spokes = 
    visualize_info(
        "Spoke", PART_2, hub, layout, show_parts); 

visualization_clamp_gear = 
    visualize_info(
        "Clamp Gear", PART_3, clamp_gear, layout_from_mode(layout), show_parts); 

//visualization_slide = 
//    visualize_info(
//        "Screw Slide", PART_4, slide, layout_from_mode(DESIGNING), show_parts); 

visualization_drive_gear = 
    visualize_info(
        "Drive Gear", PART_5, drive_gear, layout_from_mode(layout), show_parts); 

visualization_drive_gear_retainer = 
    visualize_info(
        "Drive Gear Retainer", PART_6, drive_gear_retainer, layout_from_mode(layout), show_parts);

        
visualization_drive_shaft = 
    visualize_info(
        "Clamp Drive Shaft", PART_7, drive_shaft, layout_from_mode(layout), show_parts);
        
visualization_alt_drive_gear_retainer = 
    visualize_info(
        "Alternative Drive Gear Retainer", PART_8, alt_drive_gear_retainer, layout_from_mode(layout), show_parts);        

              
        
/* Gear Calculations */

function shallow_bevel_gear_od(teeth, gear_module, cone_angle_degrees, tooth_width) = 
    teeth * gear_module * sin(cone_angle_degrees);

function shallow_bevel_gear_id(teeth, gear_module, cone_angle_degrees, tooth_width) =
    shallow_bevel_gear_od(teeth, gear_module, cone_angle_degrees, tooth_width) - 2 * tooth_width;
    
function shallow_bevel_gear_md(teeth, gear_module, cone_angle_degrees, tooth_width) = 
    shallow_bevel_gear_od(teeth, gear_module, cone_angle_degrees, tooth_width) - tooth_width;


function teeth_for_od_shallow_bevel_gear(od, gear_module, cone_angle_degrees) =
    ceil(od/(gear_module * sin(cone_angle_degrees)));
    
function teeth_for_id_shallow_bevel_gear(id, gear_module, cone_angle_degrees, tooth_width) = 
    teeth_for_od_shallow_bevel_gear(id + 2*tooth_width, gear_module, cone_angle_degrees);     

//// Function to calculate Basic Diameter (BD) of a bevel gear
//function bevel_gear_md(teeth, gear_module, cone_angle_degrees) = 
//    (bevel_gear_id(teeth, gear_module, cone_angle_degrees) + 
//    bevel_gear_od(teeth, gear_module, cone_angle_degrees)) / 2;

//echo("adjustment", 2 * sin(cone_angle_drive_gear * 2*PI/360));

//echo("id", bevel_gear_id(teeth=10, gear_module=1, cone_angle_degrees=90));
//echo("od", bevel_gear_od(teeth=10, gear_module=1, cone_angle_degrees=90));

// Calcs for values that need to be shared to calculate displacements
id_clamp_gear = (n_teeth_clamp_gear - 2) * module_clamp_gear;
    
od_clamp_gear  = (n_teeth_clamp_gear + 2) * module_clamp_gear;
    
md_clamp_gear  = (n_teeth_clamp_gear) * module_clamp_gear;



target_id_drive_gear = od_spacer;

n_teeth_drive_gear = 
    teeth_for_id_shallow_bevel_gear(
        target_id_drive_gear, 
        module_drive_gear, 
        cone_angle_drive_gear, 
        tooth_width_drive_gear);

id_drive_gear = shallow_bevel_gear_id(
    n_teeth_drive_gear, module_drive_gear, cone_angle_drive_gear, tooth_width_drive_gear);
    
od_drive_gear  = shallow_bevel_gear_od(
    n_teeth_drive_gear, module_drive_gear,  cone_angle_drive_gear, tooth_width_drive_gear);
    
md_drive_gear  = shallow_bevel_gear_md(
    n_teeth_drive_gear, module_drive_gear,  cone_angle_drive_gear, tooth_width_drive_gear);
    
flange_screw_offset = ceil(((od_drive_gear + 4)/2)/sqrt(2));
echo("flange_screw_offset", flange_screw_offset);


d_number_ten_screw = 4.7;
spoke_to_gear_clearance = 4;
dx_spoke = ceil(od_drive_gear/2 + d_number_ten_screw/2 - r_hub + spoke_to_gear_clearance); // [0 : 20]

echo("n_teeth_drive_gear", n_teeth_drive_gear);
echo("Clamp drive gear - id",  id_drive_gear);
echo("md", md_drive_gear);
echo("od", od_drive_gear);
echo("target_id_drive_gear", target_id_drive_gear);
if (show_drive_gear_construction_lines) {  
    color(COPPER) can(d=target_id_drive_gear, hollow=target_id_drive_gear-1, h=5);     
    color(BRONZE) can(d=id_drive_gear, hollow=id_drive_gear-0.5, h=5);
    color(SILVER) can(d=md_drive_gear, hollow=md_drive_gear-0.5, h=5);  
    color(GOLD) can(d=od_drive_gear, hollow=od_drive_gear-0.5, h=5);     
   
}    

dz_top_of_drive_gear = 
    md_clamp_gear/2 + h_base_drive_gear + module_drive_gear/sin(cone_angle_drive_gear);
dz_top_of_spacer = dz_top_of_drive_gear + h_spacer;

planetary_gear_ratio = n_teeth_drive_gear/n_teeth_clamp_gear;
echo("planetary_gear_ratio", planetary_gear_ratio);
range_of_rotation_drive_shaft = range_of_rotation_clamp_gear/planetary_gear_ratio; 
echo("range_of_rotation_drive_shaft", range_of_rotation_drive_shaft);

range_of_rotation_servo = 135;
required_gear_ratio_servo_transmission = range_of_rotation_drive_shaft / range_of_rotation_servo;
echo("required_gear_ratio_servo_transmission", required_gear_ratio_servo_transmission);
n_teeth_servo_transmission = ceil(n_teeth_shaft * required_gear_ratio_servo_transmission);
echo("n_teeth_servo_transmission", n_teeth_servo_transmission);
md_servo_transmission = n_teeth_servo_transmission * gear_module_shaft;
echo("md_servo_transmission", md_servo_transmission);

/*  Rendering order */

// Render from inside to outside, not by part number, for use with ghostly view


filament(as_clearance=false);
pure_vitamin_slide(center=BEHIND); 
drive_gear_retainer(show_vitamins=show_vitamins);
alt_drive_gear_retainer();

clamp_gears(show_vitamins=show_vitamins);
hub(show_vitamins=show_vitamins);
drive_gear(show_vitamins=show_vitamins);
drive_shaft(show_vitamins = true);
spokes();






/*   Mocks and separate vitamains */ 

module filament(as_clearance=false) {
    d = as_clearance ? d_filament_with_clearance : d_filament;
    alpha = as_clearance ? 0 : 1;
    if (as_clearance) {
        can(d=d, h=a_lot, $fn=12); 
    } else {
        hide = (mode == PRINTING) || (mode==DESIGNING); 
        if (show_filament && !hide) {
            color("red", alpha) {
                can(d=d, h=slide_length + 40, $fn=12);
            }
        }
    }  
}


//color("red", alpha=0.25) pure_vitamin_slide(as_clearance=true, center=BEHIND); 


module clamp_screw_nut(as_clearance=false) {
    if (as_clearance) {
        rotate([0, 90, 0]) {
            hole_through("M2", $fn = 12);
        } 
        translate([-r_nut_cut_clamp_screw, 0, 0]) {
            rotate([0, 90, 0]) {  //[0, -90, 180]
                tuned_M2_nutcatch_side_cut(as_clearance=true);
            } 
        }
        translate([-r_nut_cut_clamp_screw - 3.6, 0, 0]) 
            rod(d = d_ptfe_insertion, l = a_lot, center=BEHIND);
        
    } else {
        color(BLACK_IRON) {
            translate([-r_nut_cut_clamp_screw, 0, 0]) rotate([0, -90, 180]) {
                 nut("M2");
            }
        }          
    }            
}



module pure_vitamin_slide(as_clearance = false, center = ABOVE, show_for_design = false) {
    
    m2_nut_height = 1.6;
    m2p5_nut_height = 2;
    h_outer_ptfe_bearing = 
        l_slide_screws 
        + (d_filament/2 - clamping)
        -r_hub 
        -h_inner_ptfe_bearing
        -m2_nut_height 
        -m2p5_nut_height
        -m2_nut_height; 
    // Origin of stack is going to be at the foot of the screw
    dz_screw = 0;
    dz_ptfe_inner = dz_screw + r_hub - (d_filament/2 - clamping);
    dz_nut_1 = dz_ptfe_inner + h_inner_ptfe_bearing;
    dz_nut_2 = dz_nut_1 + m2_nut_height;
    dz_nut_3 = dz_nut_2 + m2p5_nut_height;
    dz_ptfe_outer = dz_nut_3  + m2_nut_height;
    
    echo("h_outer_ptfe_bearing", h_outer_ptfe_bearing);
    module up(dz, h) {
        translate([0, 0, dz + h]) children();
    }
    module stack() {
        up(dz_screw, l_slide_screws) color(BLACK_IRON) screw(str("M2x", l_slide_screws));
        up(dz_ptfe_inner, h_inner_ptfe_bearing) color(PTFE) can(d=od_ptfe_tube, h=h_inner_ptfe_bearing, center=BELOW);
        up(dz_nut_1,  m2_nut_height) color(BLACK_IRON) nut("M2");
        up(dz_nut_2, m2p5_nut_height) color(STAINLESS_STEEL) nut("M2.5");
        up(dz_nut_3, m2_nut_height) color(BLACK_IRON) nut("M2");
        up(dz_ptfe_outer, h_outer_ptfe_bearing) color(PTFE) can(d=od_ptfe_tube, h=h_inner_ptfe_bearing, center=BELOW);
    }
    
    module cavity() {
        can(d=d_ptfe_insertion, h=l_slide_screws, center=ABOVE);
        hull() {
            up(dz_nut_1, l_slide_screws) can(d=d_ptfe_insertion, h=l_slide_screws, center=BELOW);
            up(dz_nut_2-0.4, 0) rotate([180, 0, 0]) nutcatch_parallel("M2.5", clh = a_lot, clk=0.4);
        }        
    }
    rotation = 
        center == ABOVE ? [0, 0, 0] :
        center == BELOW ? [180, 0, 0] :
        center == FRONT ? [0, -90, 0] :
        center == BEHIND ? [0, 90, 0] :
        assert(false);
    
    translation = 
            as_clearance ? [0, 0, 0] :
            mode == PRINTING ? [0, 0, 0] : // Doesn't matter, since we don't print this
            mode == DESIGNING ? [0, 0, 0] :
            mode == MESHING_GEARS ? [dx_clamp_screw, 0, 0] :
            mode == NEW_DEVELOPMENT ? [0, 0, 0] :
            assert(false, "Not determined");  
    
    hide = (mode == PRINTING) || (mode==DESIGNING); 
    translate(translation) {
        rotate(rotation) {
            if (as_clearance) {
                cavity();
            } else {
                if (show_vitamins && !hide) {
                    stack();
                } else if (show_vitamins && show_for_design && mode == DESIGNING) {
                    stack();
                }
            }
        }
    }
}


/*   Implementation */ 

module hub(show_vitamins=true) {
    
    module cutouts() {
        rotate([0, 0, 180]) clamp_screw_nut(as_clearance=true);
        filament(as_clearance=true);        
    }
    rotation = mode == PRINTING ? [180, 0, 0] : [0, 0, 0];
    translation = mode == PRINTING ? [dx_hub_bp, dy_hub_bp, h_hub/2] : [0, 0, 0]; 
    
    translate(translation) {
        rotate(rotation) {
            if (show_vitamins) {
                visualize_vitamins(visualization_hub) {
                    rotate([0, 0, 180]) clamp_screw_nut(as_clearance=false);
                }
            }
            visualize(visualization_hub) {
                render(convexity=10) difference() {
                    can(d = 2 * r_hub, h = h_hub);
                    translate([0, 0, h_hub/2]) retention_shaft_screws(as_clearance=true, cld=0.4);  // Pass through easily
                    triangle_placement(r=0) {
                        cutouts();
                    }
                }
            }
        }
    }
}

module spokes() {
    dx_spoke_total = r_hub-2 + dx_spoke;
    echo("dx_spoke_total", dx_spoke_total);
    module shape() {
        triangle_placement(r=0) {
            rotate([0, 0, 60]) {
                translate([r_hub-2, 0, 0]) {
                    difference() {
                        hull() {
                            block([1, y_spoke_base, h_hub], center=FRONT);
                            translate([dx_spoke, 0, 0]) can(d=11, h=h_hub);
                        }
                        translate([dx_spoke, 0, 0]) can(d=4.7, h=a_lot);
                    }
                }
            }
        }
    }
    // Spokes move with hub
    rotation = [0, 0, 0];
    translation = mode == PRINTING ? [dx_hub_bp, dy_hub_bp, h_hub/2] : [0, 0, 0]; 
    translate(translation) {
        rotate(rotation) {
            visualize(visualization_spokes) {
                shape();
            }
        }
    }
}



module drive_gear(show_vitamins=true, include_bottom_gear=false) {
    dz_base = module_drive_gear/sin(cone_angle_drive_gear);
    module additions() {        
        translate([0, 0, -dz_base]) can(d=od_drive_gear, h=h_base_drive_gear, center=BELOW);     
    }
    module removals() {
        can(d = d_drive_gear_retainer_shaft + 2*clearance_drive_gear_retainer_shaft,  h = a_lot, $fn=24);
        translate([0, 0, od_clamp_gear/2-1]) rotate([180, 0, 0]) drive_shaft_screws(as_clearance=true, include_head = true);
    }
    module shape() { 

        general_bevel_gear(
                n_teeth_drive_gear, 
                module_drive_gear, 
                tooth_width_drive_gear, 
                cone_angle = cone_angle_drive_gear, 
                body_child = 0, 
                cutout_child = 1,
                add_printing_support=false) {
            additions();
            removals();
        }
    } 
    pop = explode ? 10 : 0;
    dz = md_clamp_gear/2 + pop;
    top_rotation = mode == PRINTING ? [0, 0, 0] : [180, 0, 0];
    top_translation = 
        mode == PRINTING ? [dx_drive_gear_bp, dy_drive_gear_bp, h_hub/2] : 
        [0, 0, md_clamp_gear/2 + pop];
    bottom_rotation = [0, 0, 0];
    bottom_translation = -top_translation;
    if (show_vitamins  && mode != PRINTING) {
        visualize_vitamins(visualization_drive_gear) {
            drive_shaft_screws(as_clearance=false, include_head = true);
        }
    }
    visualize(visualization_drive_gear) {
        translate(top_translation) rotate(top_rotation) shape(); 
        if (include_bottom_gear) {
            translate(bottom_translation) rotate(bottom_rotation) shape();
        }
    }
}

module clamp_gears(show_vitamins = true, include_outer_hub = true, screw_length=16) {
    if (mode == PRINTING) {
        triangle_placement(r=10) {
            clamp_gear(
                show_vitamins = show_vitamins, 
                include_outer_hub = include_outer_hub, 
                screw_length=screw_length);
        }
    } else if (mode == DESIGNING) {
        clamp_gear(
            show_vitamins = show_vitamins, 
            include_outer_hub = include_outer_hub, 
            screw_length=screw_length);
    } else if (mode == MESHING_GEARS) {
        triangle_placement(r=0) {
            clamp_gear(
                show_vitamins = show_vitamins, 
                include_outer_hub = include_outer_hub, 
                screw_length=screw_length);
        }
    }
}


module clamp_gear(show_vitamins = true, include_outer_hub = true, screw_length=16) {
    
    h_inner_hub_clamp_gear = 4; 
    dz_outer_hub = 0.2;  // Offset because of the printing support for the gear;
    z_slide_padding = 2;
    dz_nut_block = dz_outer_hub - z_slide_padding;
    h_outer_hub = 0;
    d_inner_hub = d_ptfe_insertion + 2; 
    

    module additions() {
        translate([0, 0, tooth_width_clamp_gear]) 
            translate([0, 0, -0.5]) 
                can(d=d_inner_hub, h=h_inner_hub_clamp_gear, center=ABOVE);
        if (include_outer_hub) {
            translate([0, 0, dz_outer_hub]) can(d=od_clamp_gear, h=h_outer_hub, center=BELOW);
        }
    }
    dz_plane_clearance = 0.5;
    module removals() {
        translate([0, 0, 25]) hole_through("M2", cld=0.6, $fn=12);
        //translate([0, 0, 4]) clamp_gear_slide(as_clearance=true);
        translate([0, 0, dx]) pure_vitamin_slide(as_clearance = true, center = BELOW);
        translate([0, 0, dz_plane_clearance]) plane_clearance(BELOW);
    }
    module shape() {
        general_bevel_gear(
                n_teeth_clamp_gear, 
                module_clamp_gear, 
                tooth_width_clamp_gear, 
                cone_angle = cone_angle_clamp_gear, 
                body_child = 0, cutout_child = 1) {
            additions();
            removals();
        }
    }
    module vitamins(dx) {
        translate([0, 0, dx]) pure_vitamin_slide(as_clearance = false, center = BELOW, show_for_design = true);
        //net_dx = -screw_length + dx - d_filament/2 + 0.1;
        //color(STAINLESS_STEEL) translate([0, 0, net_dx]) rotate([180, 0, 0]) m2_screw(screw_length) ;
    }
    
    
    rotation = 
        mode == PRINTING ? [0, 0, 0] :
        mode == DESIGNING ? [0, 0, 0] :
        mode == MESHING_GEARS ? [0, -90, 0] :
        mode == NEW_DEVELOPMENT ? [0, 0, 0] :
        assert(false, "Not determined");
    pop = explode ? 10 : 0;
    dx = od_drive_gear/2  + pop;
    dz_printing = h_outer_hub == 0 ? -dz_plane_clearance : h_outer_hub;
    translation =  
        mode == PRINTING ? [dx_clamp_gear_bp, dy_clamp_gear_bp, dz_printing] :
        mode == DESIGNING ? [0, 0, 0] :
        mode == MESHING_GEARS ? [dx, 0, 0] :
        mode == NEW_DEVELOPMENT ? [0, 0, 0] :
        assert(false, "Not determined");
    translate(translation) {
        rotate(rotation) {
            if (show_vitamins && mode != PRINTING) {
                visualize_vitamins(visualization_clamp_gear) 
                    vitamins(dx);
            }
            visualize(visualization_clamp_gear)
                shape();
        }
    }
}


module retention_shaft_screws(as_clearance=true, cld=0.4, screw_length = 10) {    
    r_retention_screws = 4;
    nut_tightness = screw_length - 6.5 - h_hub;
    triangle_placement(r=0) {
        rotate([0, 0, 60]) {
            translate([r_retention_screws, 0, -h_hub-2]) {
                m2_screw(
                    screw_length, 
                    head_is = BELOW, 
                    nut_tightness = nut_tightness, 
                    as_clearance = as_clearance, 
                    nut_catch = FRONT);
            }
        }
    }
}


module drive_shaft_screws(as_clearance=true, include_head = true, cld=0.4, screw_length = 16) {
    dz = md_clamp_gear/2;
    nut_tightness = screw_length/2- h_hub/2 - 2 ;
    triangle_placement(r=0) {
        rotate([0, 0, 60]) {
            translate([r_drive_shaft_screws, 0, dz]) {
                m2_screw(
                    screw_length, 
                    head_is = BELOW, 
                    nut_tightness = nut_tightness, 
                    as_clearance = as_clearance, 
                    nut_catch = ABOVE);
            }
        }
    }
}


module drive_gear_retainer(
        show_vitamins = true,
        as_clearance = false, 
        clearance = 1) {
    // Provides feature to retain the gear the nut block, 
    // the inner axle for drive gear to rotate on.
    
    // The clearance is generous, since it is just used to avoid
    // interference between the shaft (which rotates a lot to 
    // open and close the clamp), and the retainer (which only
    // rotates if the filament gets stuck on something and filament
    // rotation is used to get past the obstacle(. 
    h_drive_gear_total_base = 3;
    h_width_of_m2_screw_head = 3.8;
    retainer_clearance = 0.5;
    h_shaft = 
        od_clamp_gear/2 
        - s_nut_block/2 
        + h_drive_gear_total_base 
        + h_width_of_m2_screw_head/2 + retainer_clearance;
    dz_screws = 4;
    d_cap = d_drive_gear_retainer_shaft + 2;
    
    id_spacer = d_cap + clearance_for_d_cap;  

    
    
    module filament_entrance() {
        translate([0, 0, h_shaft]) can(d=d_ptfe_insertion, h=4, center=BELOW, rank = 10);
        translate([0, 0, h_shaft-4]) can(d=d_filament, taper= d_ptfe_insertion, h=2, center=BELOW);        
    }
    module blank() {
        can(d=d_drive_gear_retainer_shaft, h=h_shaft, center=ABOVE);
        translate([0, 0, h_shaft]) 
            can(d = d_cap, h = h_drive_gear_retainer_cap, center=BELOW);
                     
    }
    module exit_shape() {
        difference() {        
            mirror([0, 0, 1]) blank();
            filament(as_clearance=true);   
            translate([0, 0, s_nut_block]) retention_shaft_screws(as_clearance=true, screw_length=l_shaft_screws);
        }
    }
    
    module drive_shaft_side_shape() {
        difference() { 
            blank();
            filament(as_clearance=true);
            filament_entrance();
            translate([0, 0, 0]) 
            retention_shaft_screws(as_clearance=true, screw_length=l_shaft_screws);  
        }         
    }
    
    module spacer() {
        
        difference() {
            translate([0, 0, h_shaft]) can(d = od_spacer, center=BELOW, h = h_spacer);
            drive_shaft_screws(as_clearance=true);
            can(d = id_spacer, h = a_lot);            
        }
    }
    
    if (as_clearance) {
        can(d = d_drive_gear_retainer_shaft + 2 * clearance, h=h_shaft, center=ABOVE);
        can(d = d_ptfe_insertion, h = h_shaft + 4, center=ABOVE);
    } else {
        rotation = mode == PRINTING ? [180, 0, 0] : [0, 0, 0];
        pop = explode ? 20 : 0;
        dz = s_nut_block/2 + pop;
        translation = 
            mode == PRINTING ? [dx_drive_gear_retainer, dy_drive_gear_retainer, h_shaft] :
            [0, 0, dz];
        translate(translation) {
                rotate(rotation) {
                if (show_vitamins && mode != PRINTING) {
                    visualize_vitamins(visualization_drive_gear_retainer) {
                        translate([0, 0, 0]) retention_shaft_screws(as_clearance=false, screw_length=l_shaft_screws); 
                    }
                }
                visualize(visualization_drive_gear_retainer) {
                    if (include_drive_shaft_side) {
                        drive_shaft_side_shape();
                    }
                    if (include_drive_gear_spacer) {
                        spacer();
                    }
                }
            }
        }
        translate([0, 0, -dz]) {
            visualize(visualization_drive_gear_retainer) {
                if (include_exit_side) {
                    exit_shape();
                }
            }
        }
    }
}




module drive_shaft(show_vitamins = true) {
    h_allowance_for_screws = 5;
    h_retainer_cap =14.5;
    h_attachment = 2;
    module shaft() {
        translate([0, 0, gear_height_shaft/2]) 
            general_straight_spur_gear(
                n_teeth_shaft, 
                gear_module_shaft, 
                gear_height_shaft, 
                body_child = -1, 
                cutout_child = -1);
    }

    module flange() {
        can(d = od_flange, h = 2, center=ABOVE);
    }
    module blank() {
        shaft();
        flange(); 
    }
    module shape() {
        difference() {
            blank();
            filament(as_clearance=true);
            translate([0, 0, -10]) drive_shaft_screws(as_clearance=true);
        }
    }
    translation =  
        mode == PRINTING ? [dx_drive_shaft_bp, dy_drive_shaft_bp, 0] :
        [0, 0, dz_top_of_spacer]; // Just do assembled for now!
    visualize(visualization_drive_shaft)
        translate(translation) shape();
}



module alt_drive_gear_retainer() {
    dx_total_spoke = 24;
    module shape() {
        difference() {
            union() {
                hull() {
                    triangle_placement(r=dx_total_spoke) can(d=8,  h=1, center=ABOVE);
                }
                triangle_placement(r=dx_total_spoke) can(d=12,  h=2, center=ABOVE);
            }
            can(d=od_spacer + 1, h=a_lot);
            triangle_placement(r=dx_total_spoke) can(d=8,  h=a_lot); 
        }
    }
    rotation = [0, 0, 0];
    translation = [0, 0, 0];
    visualize(visualization_alt_drive_gear_retainer) {
        translate(translation) {
            rotate(rotation) {
                shape();
            }
        }    
    }
}


drive_shaft_base();

module  drive_shaft_base() {
    dx_total_spoke = 24;
    module blank() {
        triangle_placement(r=0) {
            hull() {
                can(d=4, h=1); 
                translate([dx_total_spoke, 0, 0]) can(d=4, h=1); 
            }
            can(d=8, h=1); 
        } 
    }   
    module shape() {
        difference() {
            blank();
//            union() {
//                hull() {
//                    triangle_placement(r=dx_total_spoke) can(d=8,  h=1, center=ABOVE);
//                }
//                triangle_placement(r=dx_total_spoke) can(d=12,  h=2, center=ABOVE);
//            }
//            can(d=od_spacer + 1, h=a_lot);
//            triangle_placement(r=dx_total_spoke) can(d=8,  h=a_lot); 
        }
    }
    rotation = [0, 0, 0];
    translation = [0, 0, 0];
    visualize(visualization_alt_drive_gear_retainer) {
        translate(translation) {
            rotate(rotation) {
                shape();
            }
        }    
    }


/*   General Routines */ 

module general_bevel_gear(
        n_teeth, 
        gear_module, 
        tooth_width, 
        cone_angle = 45, 
        body_child = -1, 
        cutout_child = -1, 
        add_printing_support = false) { 
    render(convexity=10) difference() {
        union() {    
            bevel_gear(
                //basic options
                n = n_teeth,  // number of teeth
                m = gear_module,   // module
                w = tooth_width,   // tooth width
                cone_angle     = cone_angle,
                pressure_angle = 25,
                helix_angle    = 0,   // the sign gives the handiness
                backlash       = 0.1 // in module units
            );            
            if (body_child >= 0 && $children > body_child) {
                children(body_child);
            }
            // print support
            if (add_printing_support) {
                translate([0, 0, -0.4]) spur_gear(
                    n = n_teeth,  // number of teeth
                    m = gear_module,   // module
                    z=1);
            }
        }
        if (cutout_child >= 0 && $children > cutout_child) {
            children(cutout_child);
        }  
    }
}



module general_straight_spur_gear(n_teeth, gear_module, gear_height, body_child = -1, cutout_child = -1) {
    render(convexity=10) difference() {
        union() {
            spur_gear(
                n = n_teeth,  // number of teeth, just enough to clear rider.
                m = gear_module,   // module
                z = gear_height,   // thickness
                pressure_angle = 25,
                helix_angle    = 0,   // the sign gives the handiness, can be a list
                backlash       = 0.1 // in module units
            );
            if (body_child >= 0 && $children > body_child) {
                children(body_child);
            }
        }
        if (cutout_child >= 0 && $children > cutout_child) {
            children(cutout_child);
        }  
    }
}