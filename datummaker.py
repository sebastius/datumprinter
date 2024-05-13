#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import argparse

def create_date_image(toptext="", toptextsize=40, offset_days=0, date_format="YYYY-MM-DD", date_size=40, font_path="./arial.ttf", text_color=(0, 0, 0), background_color=(255, 255, 255)):
    current_date = datetime.now() + timedelta(days=offset_days)
    current_date_str = current_date.strftime(date_format)
    font_text = ImageFont.truetype(font_path, toptextsize)
    font_date = ImageFont.truetype(font_path, date_size)

    text_left, text_top, text_right, text_bottom = font_text.getbbox(toptext)
    date_left, date_top, date_right, date_bottom = font_date.getbbox(current_date_str)
    
    width = max(text_right, date_right)
    height = text_bottom + 10 + date_bottom
    image_size = (width,height)
    image = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(image)

    toptext_x = (image_size[0] - text_right) / 2
    toptext_y = 0
    date_x = (image_size[0] - date_right) / 2
    date_y = text_bottom + 10

    draw.text((toptext_x, toptext_y), toptext, anchor="lt", fill=text_color, font=font_text)
    draw.text((date_x, date_y), current_date_str, anchor="lt", fill=text_color, font=font_date)

    return image

def main():
    parser = argparse.ArgumentParser(description='Generate an image with current date')
    parser.add_argument('--format', '-f', default='%d-%m-%y', help='Date format (e.g., %d-%m-%y)')
    parser.add_argument('--output', '-o', default='current_date.png', help='Output image filename')
    parser.add_argument('--text', '-t', default=' ', help='Specify a text above the date')
    parser.add_argument('--textsize', '-ts', default=40, help='Specify the font size for the text line')
    parser.add_argument('--datesize', '-ds', default=40, help='Specify the font size for the date')
    parser.add_argument('--offset', '-x', default=0, help='Specify the offset in days from today')
    args = parser.parse_args()
    image = create_date_image(toptext=args.text, toptextsize=int(args.textsize), offset_days=int(args.offset), date_size=int(args.datesize), date_format=args.format)
    image.save(args.output)
    print(f"Image saved as {args.output}")

if __name__ == "__main__":
    main()
