import os
from dotenv import load_dotenv


def list_html_list(lst):
    start = '<!-- wp:list --><ul>'
    for elem in lst:
        start += f'<!-- wp:list-item --><li>{elem}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code

# print(list_html_list(['1','2','3']))


def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key,value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}</strong>:  {value.title()}</li><!-- /wp:list-item -->'

    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code

# print(dict_list({'name': 'john', 'age': '32'}))


def headers():
    import base64
    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    header = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return header


def image_url(src,name):
    first_line = '<!-- wp: image{"align": "center", "sizeSlug": "large"} -->'
    second_line = f'<figure class ="wp-block-image aligncenter size-large"> <img src="{src}" alt="{name}+image"/>'
    third_line = f'<figcaption class ="wp-element-caption">{name}</figcaption> </figure><!--/wp: image -->'
    code = first_line + second_line + third_line

    return code


def wp_h2(text):
    return f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'


def wp_para(text):
    return f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->"


def openai_text(prompt):

    load_dotenv()
    import openai
    openai.api_key = os.getenv('API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    data = response.get('choices')[0].get('text').strip()
    code = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
    return code


# print(openai_text('Write a 150 words conclusion about How Japan Airlines Nearly Collapsed'))