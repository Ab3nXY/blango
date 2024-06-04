Demo Website: [BlogApp](https://ab3nxy.pythonanywhere.com/)        Demo Video: [BlogApp on Youtube](https://youtu.be/92fWLih0-Ws)

![Landing Page](https://github.com/Ab3nXY/blango/assets/127937158/d298b581-e749-4462-a5f6-cfa19baff10a)
![Registration](https://github.com/Ab3nXY/blango/assets/127937158/cee6aed1-721a-40ec-a257-76f97d0ac30b)
![Login](https://github.com/Ab3nXY/blango/assets/127937158/8cf34b7a-15e2-4d91-a249-3a86c4f2ed5d)
![Creat Blog](https://github.com/Ab3nXY/blango/assets/127937158/a7679486-d6f6-4291-9419-acfc8bb2fba7)
![Blog detail](https://github.com/Ab3nXY/blango/assets/127937158/5d43ff7e-5336-4ef7-9fdd-23f1078a4d46)
![Comment and share section](https://github.com/Ab3nXY/blango/assets/127937158/e963538e-fd52-4c5d-8d41-5bb538bcb25f)
![DRF](https://github.com/Ab3nXY/blango/assets/127937158/a74c901a-adec-4561-924a-f4af496ddf23)
![DRF blogs](https://github.com/Ab3nXY/blango/assets/127937158/f51a922e-826f-48bb-bc9a-4b3fc89b8594)
![DRF filter](https://github.com/Ab3nXY/blango/assets/127937158/04b6fe8b-8b04-4005-ab45-66ac26ae1433)

# Blango: A Blog Writing App with REST API and IBM watson for sentimental analysis
## Features

- **Post creation:** Users can create new blog posts with titles, content, categories, and images.
- **Post editing:** Users can edit existing blog posts, modifying titles, content, categories, publication status, and images.
- **Post deletion:** Users can delete blog posts that are no longer needed.
- **Category management:** Users can create and manage categories for their blog posts.
- **Post search:** Users can search for blog posts by title, content, or category.
- **Comment system:** Users can leave comments on blog posts and view comments left by other users.
- **Social media integration:** Users can share their blog posts on platforms like Twitter and Facebook.

## REST API

The Blango REST API offers endpoints for managing blog posts, categories, and comments:

- `/api/posts/`: List, create, and retrieve blog posts.
- `/api/posts/<id>/`: Update and delete a blog post.
- `/api/categories/`: List, create, and retrieve blog categories.
- `/api/comments/`: List, create, and retrieve blog comments.

Authentication is implemented using JSON Web Tokens (JWTs), and authorization utilizes the Django REST Framework's permissions system.

## Django REST Framework Features

Blango incorporates several Django REST Framework features, showcasing advanced capabilities:

- **Model serializers:** Blango uses model serializers for efficient serialization and deserialization of blog post data in JSON format.
- **Viewsets:** Viewsets provide a unified interface for managing blog posts, enhancing the app's modularity.
- **Routers:** Automatic URL generation for REST API endpoints is achieved through the use of routers.
- **Authentication and authorization:** Blango leverages JWTs and the Django REST Framework's permissions system for robust user authentication and authorization.


### Installation

1. Clone the repository:
   ```git clone https://github.com/ab3nxy/blango.git```
   
2. Navigate to the project directory:
   ```cd blango```

3. Install dependencies:
   ```pip install -r requirements.txt```

4. Migrate the database:
   ```python manage.py migrate```

5. Run the development server:
   ```python manage.py runserver```

