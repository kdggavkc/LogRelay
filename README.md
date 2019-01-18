# LogRoute
Assign functions to logger levels to conveniently manipulate and handle messages in one method call. Serves as a quick and easy replacement for handlers, though not as powerful.

## Examples
```
from logroute import LogRouter

def send_to_datadog(msg, **kwargs):
    event_type = kwargs.get('event_type')
    ### datadog api call ...
  
def print_all_caps(msg, **kwargs):
    print msg.upper()

R = LogRouter('my relay')
R.setRoutes([30], [send_to_datadog, print_all_caps])
R.WARNING('Important alert!', event_type='MEMORY LOW')
```
