import json
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageOps import scale
import math





#Make Image
def generate_images(group_data, total_mice, strain, experiment_title, institution, pi_name):

            #mice info
            mice_info = {'subjects': total_mice}
            strain_info = {'strain': strain}
          
            #Make Image
            image = Image.new('RGB', (1300, 900), 'white')
            draw = ImageDraw.Draw(image)

            #Font
            font_path = "./fonts/ARIAL.TTF"
            font_size = 15
            fontW = ImageFont.truetype(font_path, font_size)

            #Title Font
            title_font_size = 30
            title_font = ImageFont.truetype(font_path, title_font_size)

            #Description Font
            caption_font_size = 11
            caption_font = ImageFont.truetype(font_path, caption_font_size)

            

            #Title
            text = f"{experiment_title} Experimental Design"
            draw.text((380, 5), text, fill='black', font=title_font)

            #Draw Mouse Icon
            mouse_icon_path = 'mouse_folder/mouse_icon.png'
            mouse_icon = Image.open(mouse_icon_path)
            new_mouse_size = (150, 125)
            mouse_icon_resized = mouse_icon.resize(new_mouse_size)
            image.paste(mouse_icon_resized, (20, 350 - 50), mouse_icon_resized.convert('RGBA'))
            draw.text((20, 475 - 50), f"Number of Subjects: {mice_info['subjects']}", fill='black', font=fontW)
            draw.text((20, 500 - 50), f"Strain: {strain_info['strain']}", fill='black', font=fontW)
            

            #Draw Experiment Location
            location_picture_path = f'icon_folder/{institution}.png'
            location_picture = Image.open(location_picture_path)
            original_width, original_height = location_picture.size
            new_location_size = (int(original_width / 2), int(original_height / 2))
            location_picture_resized = location_picture.resize(new_location_size)
            image.paste(location_picture_resized, (20, 700), location_picture_resized.convert('RGBA'))
            
            #NASA Icon
            location_picture_path = 'icon_folder/NASA.png'
            location_picture = Image.open(location_picture_path)
            new_location_size = (int(245 / 2), int(205 / 2))
            location_picture_resized = location_picture.resize(new_location_size)
            image.paste(location_picture_resized, (1150, 20), location_picture_resized.convert('RGBA'))


            #NBISC Icon
            location_picture_path = 'icon_folder/nbisc_logo.png'
            location_picture = Image.open(location_picture_path)
            new_location_size = (int(200 / 2), int(200 / 2))
            location_picture_resized = location_picture.resize(new_location_size)
            image.paste(location_picture_resized, (20, 30), location_picture_resized.convert('RGBA'))
            
            
            #Display Weeks
            def display_weeks():
                max_duration = 0
                min_duration = float('inf')
                for group in group_data:
                    # Check if the current duration is greater than the current max_duration
                    if group['duration'] > max_duration:
                        # Update max_duration with the higher value
                        max_duration = group['duration']
                    if group['duration'] < min_duration:
                        # Update max_duration with the higher value
                        min_duration = group['duration']
            
                factor = (max_duration - min_duration) / 3
                factor = int(factor)
                start = min_duration
                v = 450
                y = 60
                for week in range(4):
                    if week == 3:
                        draw.text((v, y), f"Week {max_duration}", fill='black', font=fontW)
                    else:
                        draw.text((v, y), f"Week {start}", fill='black', font=fontW)
                    start += factor
                    v += 150

            display_weeks()
            
            # Function to convert duration in weeks to arrow length
            def duration_to_arrow_length(duration_weeks, min_length=50, max_length=460):
                max_duration = 0
                min_duration = float('inf')
                for group in group_data:
                    # Check if the current duration is greater than the current max_duration
                    if group['duration'] > max_duration:
                        # Update max_duration with the higher value
                        max_duration = group['duration']
                    if group['duration'] < min_duration:
                        # Update max_duration with the higher value
                        min_duration = group['duration']
                min_weeks = min_duration
                max_weeks = max_duration
                if (max_weeks - min weeks) == 0:
                            min_weeks = 1
                length = ((duration_weeks - min_weeks) / (max_weeks - min_weeks)) * (max_length - min_length) + min_length
                return max(min_length, min(length, max_length))
            
            x, y = (430, 100)

            radiation_icon = Image.open('icon_folder/radiation_icon.png')
            base_width, base_height = 30, 30
            new_width, new_height = 30, 30
            size_increment = 3
            u = (280)

            # Outputting Radiation Symbols
            for index, group in enumerate(group_data):
                current_grey = group['grey']

                # Check if this is not the first element, then compare
                if index > 0 and current_grey > group_data[index - 1]['grey']:
                    # Only update size if current grey is greater than the previous grey
                    new_width = base_width + (index * size_increment)
                    new_height = base_height + (index * size_increment)
                    resized_icon = radiation_icon.resize((new_width, new_height))

                    # Paste the resized radiation icon onto the image
                    image.paste(resized_icon, (x, y), resized_icon.convert('RGBA'))
                    
                else:
                    # If not greater, use the base size or handle it differently
                    new_width, new_height = base_width, base_height
                    resized_icon = radiation_icon.resize((base_width, base_height))
                    image.paste(resized_icon, (x, y), resized_icon.convert('RGBA'))

                draw.text((x, y + new_height + 10), f"{group['grey']} {group['units']}", fill='black', font=fontW)
                
                # Drawing Arrow
                # Extract duration in weeks from the group data
                duration_weeks = int(group['duration'])
                arrow_length = duration_to_arrow_length(duration_weeks)
                arrow_start = (x + new_width, y + new_height // 2)
                arrow_end = (arrow_start[0] + arrow_length, arrow_start[1])
                draw.line([arrow_start, arrow_end], fill='black', width=2)
                # Manually draw an arrowhead at arrow_end
                arrowhead = [(arrow_end[0], arrow_end[1]), (arrow_end[0] - 10, arrow_end[1] - 10),
                            (arrow_end[0] - 10, arrow_end[1] + 10)]
                draw.polygon(arrowhead, fill='black')

                #Tissue Harvest
                tissue_icon_path = 'icon_folder/tissue_icon.jpg'
                tissue_icon = Image.open(tissue_icon_path)
                new_tissue_size = (50, 50)
                resized_tissue_icon = tissue_icon.resize(new_tissue_size)
                image.paste(resized_tissue_icon, (int(arrow_end[0]) + 10, y - 10), resized_tissue_icon.convert('RGBA'))
                draw.text((int(arrow_end[0]) + 58, y), "Tissue \nHarvest", fill='black', font=fontW)
                y += 100
                

            y = 100
            # Outputting Groups
            for group in group_data:
                title = f"{group['group']}"
                gender = f"{group['gender']}"
                num_of_mice_in_group = group['right'] - group['left'] + 1

                if (len(title) > 18):
                     title = title[:16] + '\n' + title[16:]
                     draw.text((u, y + 38), gender, fill='black', font=fontW)
                     draw.text((u, y + 55), str(num_of_mice_in_group) + " mice", fill='black', font=fontW)
                else:
                     draw.text((u, y + 20), gender, fill='black', font=fontW)
                     draw.text((u, y + 38), str(num_of_mice_in_group) + " mice", fill='black', font=fontW)
                draw.text((u, y), title, fill='black', font=fontW)
                y += 100

            #Icon Key
            radiation_icon_key_scale = (50, 50)
            radiation_icon_key = radiation_icon.resize(radiation_icon_key_scale)
            image.paste(radiation_icon_key, (20, 625 - 100), radiation_icon_key.convert('RGBA'))
            draw.text((20, 675 - 90), "Radiation", fill='black', font=fontW)
          
            image.save('output.png')
            return image
