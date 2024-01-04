import pandas as pd
import os

output_file = 'pixilart_filtered.csv'


df = pd.read_csv(output_file, header=None)

# column 0 is the index
# column 1 is the column count
# column 2 is the row count
# column 3 is the pixel size
# column 4 is the image name
# column 5 is the image description
# column 6 is the likes count
# column 7 is the comments count

df.columns = ['index', 'column_count', 'row_count', 'pixel_size', 'title', 'description', 'likes_count', 'comments_count', 'url']



df.head()

images_without_title = df[df["title"].isnull()]
indices_to_delete = images_without_title.index.tolist()

images_without_description = df[df["description"].isnull()]
indices_to_delete += images_without_description.index.tolist()


images_with_0_likes_and_0_comments = df[(df["likes_count"] == 0) & (df["comments_count"] == 0)]
indices_to_delete += images_with_0_likes_and_0_comments.index.tolist()

print(len(indices_to_delete))

df[~df['description'].isin(indices_to_delete)]
for i in indices_to_delete:
    if os.path.exists(f'./images/pixilart/{i}.png'):
        os.remove(f'./images/pixilart/{i}.png')
    # remove from csv
    print(f'Removing {i}')
    # remove row from dataframe


df.to_csv(output_file, index=False, header=False)