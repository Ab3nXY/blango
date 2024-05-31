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

