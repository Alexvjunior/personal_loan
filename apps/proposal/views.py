from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.proposal.models import Proposal
from apps.proposal.serializers import ProposalSerializer
from apps.proposal.services import ProposalService


class ProposalViewSet(viewsets.ModelViewSet):
    serializer_class = ProposalSerializer
    service = ProposalService()
    queryset = Proposal.objects.all()
    http_method_names = ["post", "get", "patch"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        self.service.publish_message(dict(serializer.data))
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
