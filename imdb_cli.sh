api="c927a8c2"
title() {
    TITLE="$1"
    wget -qO- "http://www.omdbapi.com/?apikey=$api&t=$TITLE"
}
actor() {
    ACTOR="$1"
    wget -qO- "http://www.omdbapi.com/?apikey=$api&actor=$ACTOR"
}
actors() {
    ACTORS="$@"
    wget -qO- "http://www.omdbapi.com/?apikey=$api&actors=$ACTORS"
}
id() {
    INVALID_ID="$1"
    wget -qO- "http://www.omdbapi.com/?apikey=$api&i=$INVALID_ID"
}
verify() {
    wget -qO- "http://www.omdbapi.com/?apikey=$api"
}
rate() {
    for ((i=0; i<5; i++)); do
        wget -qO- "http://www.omdbapi.com/?apikey=$api"
        sleep 1  
    done
}
main() {
    case "$1" in
        "title") 
            title "$2" ;;
        "actor") 
            actor "$2" ;;
        "actors") 
            actors "${@:2}" ;;
        "id") 
            id "$2" ;;
        "verify") 
            verify ;;
        "rate") 
            rate ;;
        *) 
            echo "Invalid command. Usage: $0 {search-movie-by: title|actor|actors|id|verify|rate}" ;;
    esac
}
#Driver to Start  
main "$@"
