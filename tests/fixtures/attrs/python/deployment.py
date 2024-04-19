from pydantic import BaseModel


class CustomDeployment(BaseModel):
    def model_dump(self) -> dict:
        return {
            'apiVersion': 'apps/v1',
            'kind': 'Deployment',
            'metadata': {'name': 'the-deployment'},
            'spec': {
                'replicas': 3,
                'template': {
                    'metadata': {'labels': {'deployment': 'hello'}},
                    'spec': {
                        'containers': [
                            {
                                'name': 'the-container',
                                'image': 'monopole/hello:1',
                                'command': [
                                    '/hello',
                                    '--port=8080',
                                    '--enableRiskyFeature=$(' 'ENABLE_RISKY)',
                                ],
                                'ports': [{'containerPort': 8080}],
                                'env': [
                                    {
                                        'name': 'ALT_GREETING',
                                        'valueFrom': {
                                            'configMapKeyRef': {
                                                'name': 'the-map',
                                                'key': 'altGreeting',
                                            }
                                        },
                                    },
                                    {
                                        'name': 'ENABLE_RISKY',
                                        'valueFrom': {
                                            'configMapKeyRef': {
                                                'name': 'the-map',
                                                'key': 'enableRisky',
                                            }
                                        },
                                    },
                                ],
                            }
                        ]
                    },
                },
            },
        }


deployment = CustomDeployment()
