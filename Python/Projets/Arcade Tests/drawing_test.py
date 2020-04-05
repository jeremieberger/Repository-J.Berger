#!/usr/bin/python3.7
# -*-coding:utf-8 -*

# Copyright Nyrlathotep 2018. All Rights reserved.

# Importation des modules

import os
import arcade

arcade.open_window(500, 500, "Test Arcade")

# Set the background color

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()  # Get ready to draw

# (The drawing code will go here.)

# Different way to draw a rectangle
# Center rectangle at (100, 320) with a width of 45 and height of 25
arcade.draw_rectangle_filled(100, 320, 45, 25, arcade.color.BLUSH)

# Rotate a rectangle
# Center rectangle at (200, 320) with a width of 45 and height of 25
# Also, rotate it 45 degrees.
arcade.draw_rectangle_filled(200, 320, 45, 25, arcade.color.BITTERSWEET, 45)

# Draw a point at (50, 380) that is 5 pixels large
arcade.draw_point(50, 380, arcade.color.RED, 5)

# Draw a line
# Start point of (75, 390)
# End point of (95, 370)
arcade.draw_line(75, 390, 95, 370, arcade.color.BLOND, 2)

# Draw a circle outline centered at (140, 380) with a radius of 18 and a line
# width of 3.
arcade.draw_circle_outline(140, 380, 18, arcade.color.WISTERIA, 3)

# Draw a circle centered at (190, 380) with a radius of 18
arcade.draw_circle_filled(190, 380, 18, arcade.color.WISTERIA)

# Draw an ellipse. Center it at (240, 380) with a width of 30 and
# height of 15.
arcade.draw_ellipse_filled(240, 380, 30, 15, arcade.color.AMBER)

# Draw text starting at (10, 350) with a size of 20 points.
arcade.draw_text("Babe", 10, 350, arcade.color.BRICK_RED, 20)

arcade.finish_render()  # Finish drawing

arcade.run()  # Keep the window up until someone closes it.

os.system("pause")
