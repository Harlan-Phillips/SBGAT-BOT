import json
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageOps import scale

#Test Data
groups = [{'group': 10, 'right': 20, 'left': 10, 'grey': 2.6, 'duration': "12 weeks"}, 
          {'group': 11, 'right': 30, 'left': 21, 'grey': 5.2, 'duration': "6 weeks"}, 
          {'group': 12, 'right': 120, 'left': 50, 'grey': 10.4, 'duration': "8 weeks"},
          {'group': 15, 'right': 820, 'left': 750, 'grey': 12.5, 'duration': "4 weeks"},
          {'group': 18, 'right': 420, 'left': 260, 'grey': 22.5, 'duration': "8 weeks"}, 
          {'group': 20, 'right': 300, 'left': 220, 'grey': 36.2, 'duration': "10 weeks"}]


mice_info = {'subjects': 750}
strain_info = {'strain': 'B6CF1'}
gender_info = {'gender': "female"}
experiment_title = {'title': "G413-13"}

#Make Image
def generate_image(group_data, animal_type, experiment_title):

            #mice info
            mice_info = {'subjects': 750}
            strain_info = {'strain': 'B6CF1'}
            gender_info = {'gender': "female"}
          
            #Make Image
            image = Image.new('RGB', (1100, 800), 'white')
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

            # Function to convert duration in weeks to arrow length
            def duration_to_arrow_length(duration_weeks, min_length=50, max_length=400):
                min_weeks = 1
                max_weeks = 12
                length = ((duration_weeks - min_weeks) / (max_weeks - min_weeks)) * (max_length - min_length) + min_length
                return max(min_length, min(length, max_length))

            #Title
            text = f"{experiment_title} Experimental Design"
            draw.text((380, 5), text, fill='black', font=title_font)

            #Draw Mouse Icon
            mouse_icon_path = 'mouse_folder/mouse_icon.png'
            mouse_icon = Image.open(mouse_icon_path)
            new_mouse_size = (150, 125)
            mouse_icon_resized = mouse_icon.resize(new_mouse_size)
            image.paste(mouse_icon_resized, (20, 350), mouse_icon_resized.convert('RGBA'))
            draw.text((20, 475), f"Number of Subjects: {mice_info['subjects']}", fill='black', font=fontW)
            draw.text((20, 500), f"strain: {strain_info['strain']}", fill='black', font=fontW)
            draw.text((20, 525), f"Gender: {gender_info['gender']}", fill='black', font=fontW)

            #Draw Experiment Location
            location_picture_path = 'location_images/lbnl_lab.jpg'
            location_picture = Image.open(location_picture_path)
            new_location_size = (int(258 / 1.4), int(173 / 1.4))
            location_picture_resized = location_picture.resize(new_location_size)
            image.paste(location_picture_resized, (20, 20), location_picture_resized.convert('RGBA'))
            draw.text((20, int(173 / 1.4) + 30), f"Experiment Location: \nLawrence Berkeley National Laboratory (LBNL)", fill='black', font=caption_font)
            #Location Icon
            location_picture_path = 'icon_folder/lbnl_logo.png'
            location_picture = Image.open(location_picture_path)
            new_location_size = (int(258 / 1.4 / 2), int(173 / 1.4 / 2))
            location_picture_resized = location_picture.resize(new_location_size)
            image.paste(location_picture_resized, (20, int(173 / 1.4) + 60), location_picture_resized.convert('RGBA'))

            #Display Weeks
            weeks_to_display = [1, 5, 8, 12]
            v = 380
            y = 60
            for week in weeks_to_display:
                draw.text((v, y), f"Week {week}", fill='black', font=fontW)
                v += 150

            x, y = (380, 100)

            radiation_icon = Image.open('icon_folder/radiation_icon.png')
            base_width, base_height = 20, 20
            size_increment = 5
            u = (280)

            # Outputting Radiation Symbols
            for index, group in enumerate(group_data):

                new_width = base_width + (index * size_increment)
                new_height = base_height + (index * size_increment)
                resized_icon = radiation_icon.resize((new_width, new_height))

                # Paste the resized radiation icon onto the image
                image.paste(resized_icon, (x, y), resized_icon.convert('RGBA'))

                draw.text((x, y + new_height + 10), f"{group['grey']} cGy", fill='black', font=fontW)
                
                # Drawing Arrow
                # Extract duration in weeks from the group data
                duration_weeks = int(group['duration'].split()[0])
                arrow_length = duration_to_arrow_length(duration_weeks)
                arrow_start = (x + new_width, y + new_height // 2)
                arrow_end = (arrow_start[0] + arrow_length, arrow_start[1])
                draw.line([arrow_start, arrow_end], fill='black', width=2)
                # Manually draw an arrowhead at arrow_end
                arrowhead = [(arrow_end[0], arrow_end[1]), (arrow_end[0] - 10, arrow_end[1] - 10),
                            (arrow_end[0] - 10, arrow_end[1] + 10)]
                draw.polygon(arrowhead, fill='black')
                y += 100

            y = 100
            # Outputting Groups
            for group in group_data:
                title = f"Group #{group['group']}"
                num_of_mice_in_group = group['right'] - group['left'] + 1

                draw.text((u, y), title, fill='black', font=fontW)
                draw.text((u, y + 20), str(num_of_mice_in_group) + " mice", fill='black', font=fontW)

                #Outputting Radiation Data



                #Tissue Harvest Icon
                tissue_icon_path = 'icon_folder/tissue_icon.jpg'
                tissue_icon = Image.open(tissue_icon_path)
                new_tissue_size = (50, 50)
                resized_tissue_icon = tissue_icon.resize(new_tissue_size)
                image.paste(resized_tissue_icon, (830, y - 10), resized_tissue_icon.convert('RGBA'))
                draw.text((880, y), "Tissue \nHarvest", fill='black', font=fontW)
                y += 100

            #Icon Key
            radiation_icon_key_scale = (50, 50)
            radiation_icon_key = radiation_icon.resize(radiation_icon_key_scale)
            image.paste(radiation_icon_key, (20, 625), radiation_icon_key.convert('RGBA'))
            draw.text((20, 675), "Radiation", fill='black', font=fontW)
          
            image.save('output.png')
            return image
