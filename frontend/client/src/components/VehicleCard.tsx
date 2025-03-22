import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Car } from "@/lib/api";
import { Users, Briefcase, GaugeCircle } from "lucide-react";
import { useLocation } from "wouter";

export interface VehicleCardProps {
  vehicle: {
    id: number;
    name: string;
    description: string;
    price: number;
    capacity: number;
    luggage: number;
    transmission: string;
    image: string;
    status: string;
    mileage: number;
  };
}

export function VehicleCard({ vehicle }: VehicleCardProps) {
  const [, setLocation] = useLocation();

  return (
    <Card className="overflow-hidden hover:shadow-lg transition-shadow">
      <img
        src={vehicle.image}
        alt={vehicle.name}
        className="w-full h-48 object-cover"
      />
      <CardHeader className="pb-2">
        <div className="flex justify-between items-start">
          <div>
            <h3 className="text-xl font-bold">{vehicle.name}</h3>
            <p className="text-sm text-muted-foreground">{vehicle.description}</p>
          </div>
          <div className="text-right">
            <div className="text-2xl font-bold">${vehicle.price}</div>
            <div className="text-sm text-muted-foreground">per day</div>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div className="flex items-center gap-2">
            <GaugeCircle className="h-4 w-4" />
            <span className="text-sm">{vehicle.mileage} km</span>
          </div>
          <div className="flex items-center gap-2">
            <span className={`inline-flex items-center rounded-full px-2 py-1 text-xs font-medium ${vehicle.status === 'available' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
              {vehicle.status}
            </span>
          </div>
        </div>
        <div className="grid grid-cols-3 gap-4 mb-4">
          <div className="flex items-center gap-2">
            <Users className="h-4 w-4" />
            <span className="text-sm">{vehicle.capacity} seats</span>
          </div>
          <div className="flex items-center gap-2">
            <Briefcase className="h-4 w-4" />
            <span className="text-sm">{vehicle.luggage} bags</span>
          </div>
          <div className="flex items-center gap-2">
            <GaugeCircle className="h-4 w-4" />
            <span className="text-sm">{vehicle.transmission}</span>
          </div>
        </div>
        <Button 
          onClick={() => setLocation(`/vehicle/${vehicle.id}`)} 
          className="w-full"
        >
          View Details
        </Button>
      </CardContent>
    </Card>
  );
}