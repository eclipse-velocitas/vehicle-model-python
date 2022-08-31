# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sdv_model.proto.seats_pb2 as seats__pb2


class SeatsStub(object):
    """*
    @brief Seats service for getting and controlling the positions of the seats and their
    components in the vehicle.
    This definition corresponds to the COVESA Vehicle Service Catalog (VSC) comfort
    seats service definition (https://github.com/COVESA/vehicle_service_catalog)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Move = channel.unary_unary(
            "/sdv.edge.comfort.seats.v1.Seats/Move",
            request_serializer=seats__pb2.MoveRequest.SerializeToString,
            response_deserializer=seats__pb2.MoveReply.FromString,
        )
        self.MoveComponent = channel.unary_unary(
            "/sdv.edge.comfort.seats.v1.Seats/MoveComponent",
            request_serializer=seats__pb2.MoveComponentRequest.SerializeToString,
            response_deserializer=seats__pb2.MoveComponentReply.FromString,
        )
        self.CurrentPosition = channel.unary_unary(
            "/sdv.edge.comfort.seats.v1.Seats/CurrentPosition",
            request_serializer=seats__pb2.CurrentPositionRequest.SerializeToString,
            response_deserializer=seats__pb2.CurrentPositionReply.FromString,
        )


class SeatsServicer(object):
    """*
    @brief Seats service for getting and controlling the positions of the seats and their
    components in the vehicle.
    This definition corresponds to the COVESA Vehicle Service Catalog (VSC) comfort
    seats service definition (https://github.com/COVESA/vehicle_service_catalog)
    """

    def Move(self, request, context):
        """* Set the desired seat position

        Returns gRPC status codes:
        * OK - Seat movement started
        * OUT_OF_RANGE - The addressed seat is not present in this vehicle
        * INVALID_ARGUMENT - At least one of the requested component positions is invalid
        * INTERNAL - A seat service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MoveComponent(self, request, context):
        """Set a seat component position

        Returns gRPC status codes:
        * OK - Seat movement started
        * OUT_OF_RANGE - The addressed seat is not present in this vehicle
        * NOT_FOUND - The addressed seat component is not supported by this seat/vehicle
        * INVALID_ARGUMENT - At least one of the requested component positions is invalid
        * INTERNAL - A seat service internal error happened - see error message for details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CurrentPosition(self, request, context):
        """Get the current position of the addressed seat

        Returns gRPC status codes:
        * OK - Seat positions returned
        * OUT_OF_RANGE - The addressed seat is not present in this vehicle
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SeatsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Move": grpc.unary_unary_rpc_method_handler(
            servicer.Move,
            request_deserializer=seats__pb2.MoveRequest.FromString,
            response_serializer=seats__pb2.MoveReply.SerializeToString,
        ),
        "MoveComponent": grpc.unary_unary_rpc_method_handler(
            servicer.MoveComponent,
            request_deserializer=seats__pb2.MoveComponentRequest.FromString,
            response_serializer=seats__pb2.MoveComponentReply.SerializeToString,
        ),
        "CurrentPosition": grpc.unary_unary_rpc_method_handler(
            servicer.CurrentPosition,
            request_deserializer=seats__pb2.CurrentPositionRequest.FromString,
            response_serializer=seats__pb2.CurrentPositionReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "sdv.edge.comfort.seats.v1.Seats", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Seats(object):
    """*
    @brief Seats service for getting and controlling the positions of the seats and their
    components in the vehicle.
    This definition corresponds to the COVESA Vehicle Service Catalog (VSC) comfort
    seats service definition (https://github.com/COVESA/vehicle_service_catalog)
    """

    @staticmethod
    def Move(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.seats.v1.Seats/Move",
            seats__pb2.MoveRequest.SerializeToString,
            seats__pb2.MoveReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def MoveComponent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.seats.v1.Seats/MoveComponent",
            seats__pb2.MoveComponentRequest.SerializeToString,
            seats__pb2.MoveComponentReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CurrentPosition(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sdv.edge.comfort.seats.v1.Seats/CurrentPosition",
            seats__pb2.CurrentPositionRequest.SerializeToString,
            seats__pb2.CurrentPositionReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
