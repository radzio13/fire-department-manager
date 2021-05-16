from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from department.exceptions import SubjectException
from department.resolvers import SubjectResolver


@api_view(['POST'])
@authentication_classes((SessionAuthentication,))
def make_comment(request):
    author = request.user
    content = request.data.get('comment')
    subject_id = request.data.get('id')
    action_type = request.data.get('actionType')

    if not content or not subject_id or not action_type:
        raise ValidationError('Fields comment, id and actionType should be filled in.')

    resolver = SubjectResolver()
    try:
        SubjectModel, CommentSubjectModel = resolver.resolve(action_type)
    except SubjectException:
        raise ValidationError(f"ActionType {action_type} doesn't recognized")

    subject = get_object_or_404(SubjectModel, pk=subject_id)

    CommentSubjectModel.objects.create(
        content=content,
        author=author,
        subject=subject
    )

    return Response({"status": True}, status=200)
