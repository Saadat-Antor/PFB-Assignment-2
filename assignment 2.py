# importing necessary modules
from requests import post
import wp_funcs as wp

# extracting keywords from file
with open("keywords.txt", "r+") as f:
    lines = f.readlines()

for line in lines:
    # contents of the wordPress post
    keyword = line.strip("\n").replace("best ", "")
    title = f'Buying guide for {keyword}'.title()  # title
    slug = title.replace(" ", "-").lower()  # slug

    # intro
    intro_heading = wp.wp_h2('Introduction')
    intro_text = wp.openai_text(f'Write a short description about {keyword}').strip().strip("\n")
    intro = intro_heading + wp.wp_para(intro_text)

    # point 1
    text = f'Why {keyword} is important?'
    p1_heading = wp.wp_h2(text)
    p1_text = wp.openai_text(text)
    p1 = p1_heading + wp.wp_para(p1_text)

    # point 2
    text = f'How to choose the {line}? Write 5 lines.'
    p2_heading = wp.wp_h2(f'How to choose the {line}?')
    p2_list = wp.openai_text(text).strip()
    p2 = p2_heading + p2_list

    # point 3
    text = f"What features should be considered while buying a {keyword}? Write 200 words."
    p3_heading = wp.wp_h2(f'features should be considered while buying a {keyword}'.title())
    p3_text = wp.openai_text(text).strip()
    p3 = p3_heading + wp.wp_para(p3_text)

    # conclusion
    text = f"Write a conclusion about {line} buying guide. Write a 200 word paragraph"
    concl_heading = wp.wp_h2('Conclusion')
    concl_text = wp.openai_text(text).strip()
    concl = concl_heading + wp.wp_para(concl_text)

    content = intro + p1 + p2 + p3 + concl  # full post contents

    data = {
        'title': title,
        'content': content,
        'slug': slug,
    }

    api_url = "https://mysite.local/wp-json/wp/v2/posts"
    res = post(api_url, data=data, headers=wp.headers(), verify=False)
    print(f"{keyword} post done!")
    # print(res.json())

    # print(title, slug)