from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault

from posts.models import Group, Post, Comment, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    """Серилизатор групп"""

    class Meta:
        fields = "__all__"
        read_only_fields = ("id",)
        model = Group


class PostSerializer(serializers.ModelSerializer):
    """Серилизатор постов"""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Серилизатор комментариев"""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("post",)


class FollowSerializer(serializers.ModelSerializer):
    """Серилизатор подписок"""

    user = serializers.SlugRelatedField(
        read_only=True, slug_field="username", default=CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = ("user", "following")
        model = Follow
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Ты уже подписан на него!",
            )
        ]

    def validate_following(self, following):
        if self.context["request"].user == following:
            raise serializers.ValidationError(
                "Ты не можете подписать подписатсья сам на себя!"
            )
        return following
