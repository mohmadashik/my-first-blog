from faker import Faker
from blog.models import Post
import factory

fake =Faker()
def add_posts(N=3):
    for i in range(N):
        fake_author = fake.name()
        fake_title=factory.fake('Lovely',nb_words=2)
        Post.objects.get_or_create(author=fake_author,
        title=fake_title,
        text=fake_text)

if __name__=='__main__':
    print('Creating Posts')
    addposts()
    print('Posts created successfully!!!')
