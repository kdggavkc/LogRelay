# LogRelay
Assign functions to logger levels to conveniently manipulate and handle messages in one method call.

## Examples
```
from logrelay import LogRelay
import logging

def send_to_datadog(msg, **kwargs):
    event_type = kwargs.get('event_type')
    ### datadog api call ...
  
def print_all_caps(msg, **kwargs):
    print msg.upper()

R = LogRelay('my relay')

# can use either logging attribute style or numeric symbol to remove logging
R.setRoutes([40], [send_to_datadog, print_all_caps]) # or R.setRoutes([logging.WARNING], [send_to_datadog, print_all_caps]) 

R.WARNING('Important alert!', event_type='MEMORY LOW')
```
