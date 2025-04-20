# Change Log for Grist Tables

Track changes to grist records through a trigger function, and view changes with
a custom widget.

## Setup

### Add change_log column and trigger formula

1. In your grist table, add a column "change_log" of type "Text"
1. add a trigger function to "change_log"
1. copy the contents of "trigger_function.py" in the trigger function
1. edit `exclude` to exclude any columns you do not want to track
  1. we recommend excluding "change_log" and any other calculated columns
1. check "Apply to new records"
1. check "Apply on record changes"
1. set "Apply on changes to:" to "Any field"

### Add view changes widget

1. Click "Add New +"
1. Click "Add Widget to Page"
1. Select "Custom" Widget
1. Select the table with "change_log"
1. Set the "Select By" to the table with "change_log"
1. Enter "https://tilde.town/~kindrobot/s/grist-change_log/view_changes_widget.html" into the "Widget URL"
1. Grant read access
1. Select the "change_log" column for "CHANGE_LOG" mapping

## LICENSE 

MDGPL