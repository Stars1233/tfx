# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Definition of execution_spec."""

from dataclasses import dataclass
from typing import Set, Text

from tensorflow.core.framework import graph_pb2


@dataclass
class ExecutionSpec:
  """A spec that stores necessary information for execution.

  An ExecutionSpec can either represent a subgraph layer or represent
  part of a remote op layer (only contains one remote op).

  Attributes:
    subgraph: A `GraphDef` proto.
    input_names: A set of input node names.
    output_names: A set of output node names.
    is_remote_op: A boolean indicating the type of the layer
                  (two types: subgraph layer or remote op layer).
  """
  subgraph: graph_pb2.GraphDef
  input_names: Set[Text]
  output_names: Set[Text]
  is_remote_op: bool
